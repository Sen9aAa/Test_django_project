# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'MyInfo'
        db.create_table(u'hello_myinfo', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('surname', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=200)),
            ('bio', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('birthday', self.gf('django.db.models.fields.DateField')()),
        ))
        db.send_create_signal(u'hello', ['MyInfo'])


    def backwards(self, orm):
        # Deleting model 'MyInfo'
        db.delete_table(u'hello_myinfo')


    models = {
        u'hello.myinfo': {
            'Meta': {'object_name': 'MyInfo'},
            'bio': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'birthday': ('django.db.models.fields.DateField', [], {}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '200'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'surname': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['hello']