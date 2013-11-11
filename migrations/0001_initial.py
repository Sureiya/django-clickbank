# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Post'
        db.create_table(u'django_clickbank_post', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('post_data', self.gf('django.db.models.fields.CharField')(max_length=4096, null=True, blank=True)),
            ('get_data', self.gf('django.db.models.fields.CharField')(max_length=4096, null=True, blank=True)),
            ('failed', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('time', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal(u'django_clickbank', ['Post'])

        # Adding model 'Notification'
        db.create_table(u'django_clickbank_notification', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('receipt', self.gf('django.db.models.fields.CharField')(unique=True, max_length=13)),
            ('role', self.gf('django.db.models.fields.CharField')(max_length=9)),
            ('transaction_type', self.gf('django.db.models.fields.CharField')(max_length=15)),
            ('transaction_vendor', self.gf('django.db.models.fields.CharField')(max_length=10, blank=True)),
            ('transaction_affiliate', self.gf('django.db.models.fields.CharField')(max_length=10, null=True, blank=True)),
            ('recieved_amount', self.gf('django.db.models.fields.DecimalField')(max_digits=8, decimal_places=2)),
            ('order_amount', self.gf('django.db.models.fields.DecimalField')(max_digits=8, decimal_places=2)),
            ('tax_amount', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=8, decimal_places=2, blank=True)),
            ('payment_method', self.gf('django.db.models.fields.CharField')(max_length=4, null=True, blank=True)),
            ('currency', self.gf('django.db.models.fields.CharField')(max_length=3)),
            ('tracking_id', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('notification_version', self.gf('django.db.models.fields.CharField')(max_length=5, null=True, blank=True)),
            ('extra_data', self.gf('django.db.models.fields.CharField')(max_length=1024, null=True, blank=True)),
            ('transaction_date', self.gf('django.db.models.fields.DateTimeField')()),
            ('post_data', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['django_clickbank.Post'], null=True, blank=True)),
            ('sender_ip', self.gf('django.db.models.fields.IPAddressField')(max_length=15, blank=True)),
            ('order_language', self.gf('django.db.models.fields.CharField')(max_length=20, null=True, blank=True)),
            ('product_title', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('product_type', self.gf('django.db.models.fields.CharField')(max_length=11)),
            ('product_id', self.gf('django.db.models.fields.CharField')(max_length=5)),
            ('verification_passed', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('parent_receipt', self.gf('django.db.models.fields.CharField')(max_length=13, null=True, blank=True)),
            ('upsell_flow', self.gf('django.db.models.fields.CharField')(max_length=20, null=True, blank=True)),
            ('rebill_amount', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=8, decimal_places=2, blank=True)),
            ('processed_payments', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('future_payments', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('next_payment_date', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('rebill_status', self.gf('django.db.models.fields.CharField')(max_length=10, null=True, blank=True)),
            ('rebill_frequency', self.gf('django.db.models.fields.CharField')(max_length=20, null=True, blank=True)),
            ('full_name', self.gf('django.db.models.fields.CharField')(max_length=510)),
            ('first_name', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('last_name', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('province', self.gf('django.db.models.fields.CharField')(max_length=2, null=True, blank=True)),
            ('postal_code', self.gf('django.db.models.fields.CharField')(max_length=16, null=True, blank=True)),
            ('city', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('country', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('country_code', self.gf('django.db.models.fields.CharField')(max_length=2, null=True, blank=True)),
            ('email', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('address1', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('address2', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('shipping_address1', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('shipping_address2', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('shipping_city', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('shipping_county', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('shipping_province', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('shipping_postal_code', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('shipping_country', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('shipping_amount', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=8, decimal_places=2, blank=True)),
        ))
        db.send_create_signal(u'django_clickbank', ['Notification'])


    def backwards(self, orm):
        # Deleting model 'Post'
        db.delete_table(u'django_clickbank_post')

        # Deleting model 'Notification'
        db.delete_table(u'django_clickbank_notification')


    models = {
        u'django_clickbank.notification': {
            'Meta': {'object_name': 'Notification'},
            'address1': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'address2': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'country': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'country_code': ('django.db.models.fields.CharField', [], {'max_length': '2', 'null': 'True', 'blank': 'True'}),
            'currency': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'email': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'extra_data': ('django.db.models.fields.CharField', [], {'max_length': '1024', 'null': 'True', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'full_name': ('django.db.models.fields.CharField', [], {'max_length': '510'}),
            'future_payments': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'next_payment_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'notification_version': ('django.db.models.fields.CharField', [], {'max_length': '5', 'null': 'True', 'blank': 'True'}),
            'order_amount': ('django.db.models.fields.DecimalField', [], {'max_digits': '8', 'decimal_places': '2'}),
            'order_language': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'parent_receipt': ('django.db.models.fields.CharField', [], {'max_length': '13', 'null': 'True', 'blank': 'True'}),
            'payment_method': ('django.db.models.fields.CharField', [], {'max_length': '4', 'null': 'True', 'blank': 'True'}),
            'post_data': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['django_clickbank.Post']", 'null': 'True', 'blank': 'True'}),
            'postal_code': ('django.db.models.fields.CharField', [], {'max_length': '16', 'null': 'True', 'blank': 'True'}),
            'processed_payments': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'product_id': ('django.db.models.fields.CharField', [], {'max_length': '5'}),
            'product_title': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'product_type': ('django.db.models.fields.CharField', [], {'max_length': '11'}),
            'province': ('django.db.models.fields.CharField', [], {'max_length': '2', 'null': 'True', 'blank': 'True'}),
            'rebill_amount': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '8', 'decimal_places': '2', 'blank': 'True'}),
            'rebill_frequency': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'rebill_status': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'receipt': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '13'}),
            'recieved_amount': ('django.db.models.fields.DecimalField', [], {'max_digits': '8', 'decimal_places': '2'}),
            'role': ('django.db.models.fields.CharField', [], {'max_length': '9'}),
            'sender_ip': ('django.db.models.fields.IPAddressField', [], {'max_length': '15', 'blank': 'True'}),
            'shipping_address1': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'shipping_address2': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'shipping_amount': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '8', 'decimal_places': '2', 'blank': 'True'}),
            'shipping_city': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'shipping_country': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'shipping_county': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'shipping_postal_code': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'shipping_province': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'tax_amount': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '8', 'decimal_places': '2', 'blank': 'True'}),
            'tracking_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'transaction_affiliate': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'transaction_date': ('django.db.models.fields.DateTimeField', [], {}),
            'transaction_type': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            'transaction_vendor': ('django.db.models.fields.CharField', [], {'max_length': '10', 'blank': 'True'}),
            'upsell_flow': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'verification_passed': ('django.db.models.fields.BooleanField', [], {'default': 'True'})
        },
        u'django_clickbank.post': {
            'Meta': {'object_name': 'Post'},
            'failed': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'get_data': ('django.db.models.fields.CharField', [], {'max_length': '4096', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'post_data': ('django.db.models.fields.CharField', [], {'max_length': '4096', 'null': 'True', 'blank': 'True'}),
            'time': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['django_clickbank']