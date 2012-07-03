'''
Common utility methods used elsewhere in the site.

'''

import hashlib
import httplib2
from django.conf import settings
from django.core.paginator import Paginator, InvalidPage, EmptyPage
import sunburnt

from eulcommon.searchutil import pages_to_show

def md5sum(filename):
    '''Calculate and returns an MD5 checksum for the specified file.  Any file
    errors (non-existent file, read error, etc.) are not handled here but should
    be caught where this method is called.

    :param filename: full path to the file for which a checksum should be calculated
    :returns: hex-digest formatted MD5 checksum as a string
    '''
    # copied from keep.common.utils
    md5 = hashlib.md5()
    with open(filename,'rb') as f:
        for chunk in iter(lambda: f.read(128*md5.block_size), ''):
             md5.update(chunk)
    return md5.hexdigest()


def pmc_access_url(pmcid):
    'Direct link to a PubMed Central article based on PubMed Central ID.'
    return 'http://www.ncbi.nlm.nih.gov/pmc/articles/PMC%s/' % (pmcid,)


def solr_interface(solr_url=None):
    if not solr_url:
        solr_url = settings.SOLR_SERVER_URL

    http_opts = {}
    if hasattr(settings, 'SOLR_CA_CERT_PATH'):
        http_opts['ca_certs'] = settings.SOLR_CA_CERT_PATH
    if getattr(settings, 'SOLR_DISABLE_CERT_CHECK', False):
        http_opts['disable_ssl_certificate_validation'] = True
    http = httplib2.Http(**http_opts)
    solr = sunburnt.SolrInterface(solr_url,
                                  http_connection=http)
    return solr



def paginate(request, query):
    '''Common pagination logic, straight out of django docs.  Takes a
    :class:`~django.http.HttpRequest` and a result set that can be
    paginated; returns a tuple of the current
    :class:`django.core.paginator.Page` (based on the request) and the
    page numbers that should be displayed (generated by
    :meth:`eulcommon.searchutil.pages_to_show`).
    '''
    paginator = Paginator(query, 10)
    # get current page number
    try:
        page = int(request.GET.get('page', '1'))
    except ValueError:
        page = 1
    # return last page if an invalid page is requested
    try:
        results = paginator.page(page)
    except (EmptyPage, InvalidPage):
        results = paginator.page(paginator.num_pages)

    # calculate page links to be shown
    show_pages = pages_to_show(paginator, page)
    return results, show_pages
