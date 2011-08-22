from django.conf import settings
from django.core.urlresolvers import reverse
from django.test import TestCase, Client
from eulfedora.server import Repository
from eulfedora.util import RequestFailed
import logging
from mock import patch, Mock
from os import path

from openemory.publication.forms import UploadForm
from openemory.publication.models import Article

TESTUSER_CREDENTIALS = {'username': 'testuser', 'password': 't3st1ng'}
pdf_filename = path.join(settings.BASE_DIR, 'publication', 'fixtures', 'test.pdf')
pdf_md5sum = '331e8397807e65be4f838ccd95787880'

logger = logging.getLogger(__name__)

class PublicationViewsTest(TestCase):
    fixtures =  ['testusers']

    def setUp(self):
        self.repo = Repository(username=settings.FEDORA_TEST_USER,
                                     password=settings.FEDORA_TEST_PASSWORD)
        self.client = Client()
        self.pids = []

    def tearDown(self):
        for pid in self.pids:
            try:
                self.repo.purge_object(pid)
            except RequestFailed:
                logger.warn('Failed to purge test object %s' % pid)

    def test_upload(self):
        # not logged in
        upload_url = reverse('publication:upload')
        response = self.client.get(upload_url)
        expected, got = 302, response.status_code
        self.assertEqual(expected, got, 'Expected %s but got %s for GET on %s (not logged in)' % \
                         (expected, got, upload_url))
        response = self.client.post(upload_url)
        expected, got = 302, response.status_code
        self.assertEqual(expected, got, 'Expected %s but got %s for POST on %s (not logged in)' % \
                         (expected, got, upload_url))

        # login as test user
        self.client.login(**TESTUSER_CREDENTIALS)
        response = self.client.get(upload_url)
        expected, got = 200, response.status_code
        self.assertEqual(expected, got, 'Expected %s but got %s for GET on %s' % \
                         (expected, got, upload_url))
        self.assert_(isinstance(response.context['form'], UploadForm),
                     'upload form should be set in response context on GET')
        # invalid post - no file
        response = self.client.post(upload_url)
        self.assertContains(response, 'field is required',
             msg_prefix='required field message should be displayed when the form is submitted without data')

        # POST a test pdf
        with open(pdf_filename) as pdf:
            response = self.client.post(upload_url, {'pdf': pdf}, follow=True)  # follow redirect
            messages = [ str(msg) for msg in response.context['messages'] ]
            msg = messages[0]
            self.assert_(msg.startswith("Successfully uploaded article"),
                         "successful save message set in response context")
            # pull pid from message  (at end, wrapped in tags)
            tag_start, tag_end = '<strong>', '</strong>'
            pid = msg[msg.rfind(tag_start) + len(tag_start):msg.rfind(tag_end)]
            self.pids.append(pid)	# add to list for clean-up in tearDown

        # inspect created object
        obj = self.repo.get_object(pid, type=Article)
        # check object initialization
        self.assertEqual('test.pdf', obj.label)
        self.assertEqual('test.pdf', obj.dc.content.title)
        self.assertEqual(TESTUSER_CREDENTIALS['username'], obj.owner)
        self.assertEqual('application/pdf', obj.pdf.mimetype)
        # pdf contents
        with open(pdf_filename) as pdf:
            self.assertEqual(pdf.read(), obj.pdf.content.read())
        # checksum
        self.assertEqual(pdf_md5sum, obj.pdf.checksum)
        self.assertEqual('MD5', obj.pdf.checksum_type)
            
        # test ingest error with mock
        mock_article = Mock(Article)
        mock_article.return_value = mock_article  # return self on init
        # create mockrequest to init RequestFailed
        mockrequest = Mock()
        mockrequest.status = 401
        mockrequest.reason = 'permission denied'
        mock_article.save.side_effect = RequestFailed(mockrequest)
        with patch('openemory.publication.views.Article', new=mock_article):
            with open(pdf_filename) as pdf:
                response = self.client.post(upload_url, {'pdf': pdf})
                self.assertContains(response, 'error uploading your document')
                messages = [ str(msg) for msg in response.context['messages'] ]
                self.assertEqual(0, len(messages),
                    'no success messages set when ingest errors')
                    
            
            
        
