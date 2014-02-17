#Add to collection file openemory/publication/management/commands/import_to_symplectic.py
# 
#   Copyright 2010 Emory University General Library
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.

import settings
from collections import defaultdict
from getpass import getpass
import logging
from optparse import make_option

from django.core.management.base import BaseCommand, CommandError
from django.core.paginator import Paginator

from eulfedora.server import Repository

from openemory.publication.models import Article, OESympImportArticle, SympDate, SympPerson, SympRelation
import requests

logger = logging.getLogger(__name__)

class Command(BaseCommand):
    '''Fetch article data for `~openemory.publication.models.Article` objects and do the following:
     1. Construct a Symplectic-Elements Article.
     2. Post this article to Symplectic-Elements via the API
     If PIDs are provided in the arguments, that list of pids will be used instead of searching fedora.
    '''
    args = "[pid pid ...]"
    help = __doc__

    option_list = BaseCommand.option_list + (
        make_option('--noact', '-n',
                    action='store_true',
                    default=False,
                    help='Reports the pid and total number of Articles that would be processed but does not really do anything.'),
        )


    def handle(self, *args, **options):
        self.verbosity = int(options['verbosity'])    # 1 = normal, 0 = minimal, 2 = all
        self.v_normal = 1

        #counters
        counts = defaultdict(int)

        #connection to repository
        repo = Repository(username=settings.FEDORA_MANAGEMENT_USER, password=settings.FEDORA_MANAGEMENT_PASSWORD)

        #Symplectic-Elements setup
        session = requests.Session()
        session.headers.update({
            'Authorization': 'Basic %s' % settings.SYMPLECTIC_KEY,
            'Content-Type': 'text/xml'
        })

        pub_url = "%s/%s" % (settings.SYMPLECTIC_BASE_URL, "/publication/records/manual")
        relation_url = "%s/%s" % (settings.SYMPLECTIC_BASE_URL, "/relationships")


        #if pids specified, use that list
        try:
            if len(args) != 0:
                pids = list(args)
                pid_set = [repo.get_object(pid=p,type=Article) for p in pids]


            else:
                #search for Articles.
                pid_set = repo.get_objects_with_cmodel(Article.ARTICLE_CONTENT_MODEL, Article)

        except Exception as e:
            raise CommandError('Error getting pid list (%s)' % e.message)

        try:
            articles = Paginator(pid_set, 20)
            counts['total'] = articles.count
        except Exception as e:
            self.output(0, "Error paginating items: : %s " % (e.message))

        #process all Articles
        for p in articles.page_range:
            try:
                objs = articles.page(p).object_list
            except Exception as e:
                #print error and go to next iteration of loop
                self.output(0,"Error getting page: %s : %s " % (p, e.message))
                counts['errors'] +=1
                continue
            for article in objs:
                try:
                    relations = [] # list of relations to articles

                    if not article.exists:
                        self.output(1, "Skipping %s because pid does not exist" % article.pid)
                        counts['skipped'] +=1
                        continue
                    if not article.is_published:
                        self.output(1, "Skipping %s because pid is not published" % article.pid)
                        counts['skipped'] +=1
                        continue
                    else:
                        self.output(1,"Processing %s" % article.pid)

                        # build article xml
                        mods = article.descMetadata.content
                        symp_pub = OESympImportArticle()

                        if mods.title_info:
                            title =  mods.title_info.title
                            if mods.title_info.subtitle:
                                title += ': ' + mods.title_info.subtitle
                            symp_pub.title = title

                        if mods.abstract:
                            symp_pub.abstract = mods.abstract.text

                        if mods.final_version and mods.final_version.doi:
                            symp_pub.doi = mods.final_version.doi.lstrip("doi:")

                        if mods.journal:
                            symp_pub.volume =mods.journal.volume.number if mods.journal.volume.number  else None
                            symp_pub.issue =mods.journal.number.number if mods.journal.number.number else None
                            symp_pub.journal = mods.journal.title if mods.journal.title else None
                            symp_pub.publisher = mods.journal.publisher if mods.journal.publisher else None

                        if mods.publication_date:
                            year, month, day = '', '', ''
                            date_info = mods.publication_date.split('-')
                            if len(date_info) >=1:
                                year = date_info[0]
                            if len(date_info) >=2:
                                month = date_info[1]
                            if len(date_info) >=3:
                                day = date_info[2]
                            pub_date = SympDate(year, month, day)

                            if not pub_date.is_empty():
                                symp_pub.publication_date = pub_date

                        symp_pub.language = mods.language if mods.languages else None
                        symp_pub.keywords = [k.topic for k in mods.keywords]

                        for a in mods.authors:
                            fam = a.family_name if a.family_name else ''
                            given = a.given_name if a.given_name else ''
                            symp_pub.authors.append(SympPerson(last_name=fam, initials="%s%s" % (given[0].upper(), fam[0].upper())))
                            if a.id:
                                relations.append(
                                    SympRelation("publication(source-manual,pid-%s)" % article.pid,
                                                 "user(username=%s)" % a.id,
                                                 type_name=SympRelation.PUB_AUTHOR
                                    )
                                )



                        # post article xml
                        url = '%s/%s%' % (pub_url, article.pid)
                        status = None
                        if not options['noact']:
                            response = session.post(url, verify=False, data=symp_pub.serialize())
                            status = response.status_code
                        self.output(2,"POST %s %s" %  (url, status if status else "<NO ACT>"))
                        self.output(2, "=====================================================================")
                        self.output(2, symp_pub.serialize(pretty=True))
                        self.output(2,"---------------------------------------------------------------------")

                        # post relationship xml
                        for r in relations:
                            url = relation_url
                            status = None
                            if not options['noact']:
                                response = session.post(relation_url, verify=False, data=r.serialize())
                                status = response.status_code

                            self.output(2,"POST %s %s" %  (url, status if status else "<NO ACT>"))
                            self.output(2,r.serialize(pretty=True))
                            self.output(2,"---------------------------------------------------------------------")
                        self.output(2,"=====================================================================")

                except Exception as e:
                    self.output(0, "Error processing pid: %s : %s " % (article.pid, e.message))
                    counts['errors'] +=1

        # summarize what was done
        self.stdout.write("\n\n")
        self.stdout.write("Total number selected: %s\n" % counts['total'])
        self.stdout.write("Skipped: %s\n" % counts['skipped'])
        self.stdout.write("Errors: %s\n" % counts['errors'])


    def output(self, v, msg):
        '''simple function to handle logging output based on verbosity'''
        if self.verbosity >= v:
            self.stdout.write("%s\n" % msg)
