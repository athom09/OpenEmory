from django.db import models
from django.core.files.base import ContentFile
from django.contrib.auth.models import User
from eulfedora.server import Repository
from openemory.harvest.entrez import EntrezClient, ArticleQuerySet
from openemory.publication.models import Article


class HarvestRecord(models.Model):
    STATUSES = ('harvested', 'ingested', 'ignored')
    STATUS_CHOICES = [(val, val) for val in STATUSES]
    pmcid = models.IntegerField('PubMed Central ID', unique=True, editable=False)
    authors = models.ManyToManyField(User)
    title = models.TextField('Article Title')
    harvested = models.DateTimeField('Date Harvested', auto_now_add=True, editable=False)
    status = models.CharField(choices=STATUS_CHOICES, max_length=25,
                              default=STATUSES[0])
    fulltext = models.BooleanField(editable=False)
    content = models.FileField(upload_to='harvest/%Y/%m/%d')
    # file storage for the full Article XML fetched from PMC
    
    class Meta:
        permissions = (
            # add, change, delete are avilable by default
            ('view_harvestrecord', 'Can see available harvested records'),
        )

    def __unicode__(self):
        return u'%s (PMCID:%d, %s)' % (self.title, self.pmcid, self.status)

    @property
    def access_url(self):
        'Direct link to this PubMed Central article, based on PubMed Central ID.'
        return 'http://www.ncbi.nlm.nih.gov/pmc/articles/PMC%d/' % self.pmcid


    @staticmethod
    def init_from_fetched_article(article):
        '''Initialize a new
        :class:`~openemory.harvest.models.HarvestRecord` instance based
        on information from an
        :class:`~openemory.harvest.entrez.EFetchArticle`.

        :returns: saved :class:`HarvestRecord` instance
        '''

        record = HarvestRecord(title=article.article_title,
                               pmcid=article.docid,
                               fulltext=article.fulltext_available)
        if article.identifiable_authors():
            # record must be saved before we can add relation to authors
            record.save()
            record.authors = article.identifiable_authors()

        # save article xml as a file associated with this record
        record.content.save('%d.xml' % article.docid,
                            ContentFile(article.serialize(pretty=True)))
        record.save()
        return record


    def as_publication_article(self):
        '''Initialize (but do not save) a new
        :class:`~openemory.publication.models.Article` instance and
        based on harvested record information and Article XML.

        :returns: unsaved :class:`~openemory.publication.models.Article`
        '''
        repo = Repository()
        article = repo.get_object(type=Article)
        # using comma-delimited usernames to indicate object has multiple owners
        # should work with existing XACML owner policy;
        # for more detail, see https://jira.duraspace.org/browse/FCREPO-82
        article.owner = ', '.join(auth.username for auth in self.authors.all())
        # VERY preliminary, minimal metadata mapping 
        article.label = self.title
        article.dc.content.title = self.title
        article.dc.content.creator_list.extend([auth.get_full_name()
                                                for auth in self.authors.all()])
        article.dc.content.identifier = self.access_url

        # set the XML article content as the contentMetadata datastream
        # - record content is a file field with a read method, which should be
        #   handled correctly by eulfedora for ingest
        article.contentMetadata.content = self.content
        # TODO: format uri for this datastream ? 

        return article
    

class OpenEmoryEntrezClient(EntrezClient):
    '''Project-specific methods build on top of an
    :class:`~openemory.harvest.entrez.EntrezClient`.
    '''
    # FIXME: This doesn't feel like a "model" per se, but not sure precisely
    # where else it belongs...

    def get_emory_articles(self):
        '''Search Entrez for Emory articles, currently limited to PMC
        articles with "emory" in the affiliation metadata.

        :returns: :class:`~openemory.harvest.entrez.ESearchResponse`
        '''
        search_result = self.esearch(
            usehistory='y', # store server-side history for later queries
            db='pmc',       # search PubMed Central
            term='emory',   # for the term "emory"
            field='affl',   # in the "Affiliation" field
        )
        qs = ArticleQuerySet(self, search_result, 
            db='pmc',       # search PubMed Central
            usehistory='y', # use stored server-side history
            WebEnv=search_result.webenv,
            query_key=search_result.query_key,
        )
            
        return qs
