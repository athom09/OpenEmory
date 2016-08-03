# file openemory/publication/migrations/0008_add_license_to_site_admin.py
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

# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import DataMigration
from django.db import models
from django.contrib.auth.models import Group, Permission

class Migration(DataMigration):

    def forwards(self, orm):
        add_perm= Permission.objects.get(codename='add_license')
        change_perm = Permission.objects.get(codename='change_license')
        delete_perm = Permission.objects.get(codename='delete_license')

        g = Group.objects.get(name='Site Admin')
        g.permissions.add(add_perm)
        g.permissions.add(change_perm)
        g.permissions.add(delete_perm)
        g.save()


    def backwards(self, orm):
        add_perm= Permission.objects.get(codename='add_license')
        change_perm = Permission.objects.get(codename='change_license')
        delete_perm = Permission.objects.get(codename='delete_license')
        g = Group.objects.get(name='Site Admin')
        g.permissions.remove(add_perm)
        g.permissions.remove(change_perm)
        g.permissions.remove(delete_perm)

    models = {
        'publication.articlerecord': {
            'Meta': {'object_name': 'ArticleRecord'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'publication.articlestatistics': {
            'Meta': {'unique_together': "(('pid', 'year', 'quarter'),)", 'object_name': 'ArticleStatistics'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'num_downloads': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'num_views': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'pid': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'quarter': ('django.db.models.fields.IntegerField', [], {}),
            'year': ('django.db.models.fields.IntegerField', [], {})
        },
        'publication.featuredarticle': {
            'Meta': {'object_name': 'FeaturedArticle'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pid': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '60'})
        },
        'publication.license': {
            'Meta': {'object_name': 'License'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'short_name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'}),
            'title': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'}),
            'url': ('django.db.models.fields.URLField', [], {'unique': 'True', 'max_length': '200'}),
            'version': ('django.db.models.fields.CharField', [], {'max_length': '5'})
        }
    }

    complete_apps = ['publication']
    symmetrical = True
