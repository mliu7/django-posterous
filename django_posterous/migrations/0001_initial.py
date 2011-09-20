# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'BlogPost'
        db.create_table('django_posterous_blogpost', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('posterous_id', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('django_posterous', ['BlogPost'])


    def backwards(self, orm):
        
        # Deleting model 'BlogPost'
        db.delete_table('django_posterous_blogpost')


    models = {
        'django_posterous.blogpost': {
            'Meta': {'object_name': 'BlogPost'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'posterous_id': ('django.db.models.fields.IntegerField', [], {})
        }
    }

    complete_apps = ['django_posterous']
