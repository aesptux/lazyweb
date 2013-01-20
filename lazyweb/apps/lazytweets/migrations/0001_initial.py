# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Tweet'
        db.create_table('lazytweets_tweet', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('tid', self.gf('django.db.models.fields.BigIntegerField')()),
            ('username', self.gf('django.db.models.fields.CharField')(max_length=60)),
            ('created_at', self.gf('django.db.models.fields.CharField')(max_length=25)),
            ('content', self.gf('django.db.models.fields.CharField')(max_length=140)),
            ('url', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('img_url', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal('lazytweets', ['Tweet'])


    def backwards(self, orm):
        # Deleting model 'Tweet'
        db.delete_table('lazytweets_tweet')


    models = {
        'lazytweets.tweet': {
            'Meta': {'object_name': 'Tweet'},
            'content': ('django.db.models.fields.CharField', [], {'max_length': '140'}),
            'created_at': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'img_url': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'tid': ('django.db.models.fields.BigIntegerField', [], {}),
            'url': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'username': ('django.db.models.fields.CharField', [], {'max_length': '60'})
        }
    }

    complete_apps = ['lazytweets']