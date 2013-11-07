from django.db import models
from .settings import *
# Create your models here.

class Post(models.Model):
	""" 
	Debug model used to log raw POST dictionaries of
	clickbank data in order to create test posts
	"""
	post_data = models.CharField(max_length=4096, blank=True, null=True)
	get_data = models.CharField(max_length=4096, blank=True, null=True)
	time = models.DateTimeField(auto_now_add=True)

	class Meta:
		verbose_name = u'post'
		verbose_name_plural  = u'posts'

class Notification(models.Model):
	""" Model to hold all of the information recieved in a ClickBank Notification """

	TRANSACTION_TYPE_CHOICES = (
		('SALE', 'Sale'),
		('BILL', 'Rebill'),
		('RFND', 'Refund'),
		('CGBK', 'Chargeback'),
		('INSF', 'Insufficient Funds (eCheck)'),
		('CANCEL-REBILL', 'Cancel Rebill'),
		('UNCANCEL-REBILL', 'Resume Rebill'),
		('TEST', 'IPN Test')
	)

	ROLE_CHOICES = (
		('VENDOR', 'Vendor'),
		('AFFILIATE', 'Affiliate'),
	)

	REBILL_STATUS_CHOICES = (
		('ACTIVE', 'Active'),
		('COMPLETED', 'Completed'),
		('CANCELLED', 'Cancelled')
	)

	PRODUCT_TYPE_CHOICES = (

		)
	PAYMENT_METHOD_CHOICES = (

		)

	# Notification Fields
	receipt = models.CharField(max_length=13, unique=True)
	role = models.CharField(max_length=9, choices=ROLE_CHOICES)
	transaction_type = models.CharField(max_length=15, choices=TRANSACTION_TYPE_CHOICES)
	transaction_vendor = models.CharField(max_length=10, blank=True)
	transaction_affiliate = models.CharField(max_length=10, blank=True, null=True)
	recieved_amount = models.DecimalField(max_digits=8, decimal_places=2)
	order_amount = models.DecimalField(max_digits=8, decimal_places=2)
	tax_amount = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
	payment_method = models.CharField(max_length=4, blank=True, null=True, choices=PAYMENT_METHOD_CHOICES)
	currency = models.CharField(max_length=3)
	tracking_id = models.CharField(max_length=255, blank=True, null=True)
	notification_version = models.CharField(max_length=5, blank=True, null=True)
	extra_data = models.CharField(max_length=1024, blank=True, null=True)
	transaction_date = models.DateTimeField()
	post_data = models.ForeignKey(Post, blank=True, null=True)
	sender_ip = models.IPAddressField(blank=True)
	order_language = models.CharField(max_length=20, blank=True, null=True)
	product_title = models.CharField(max_length=255, blank=True, null=True)
	product_type = models.CharField(max_length=11, choices=PRODUCT_TYPE_CHOICES)
	product_id = models.CharField(max_length=5)

	# Upsell
	parent_receipt = models.CharField(max_length=13, blank=True, null=True)
	upsell_flow = models.CharField(max_length=20, blank=True, null=True)

	# Recurring
	rebill_amount = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
	processed_payments = models.IntegerField(blank=True, null=True)
	future_payments = models.IntegerField(blank=True, null=True)
	next_payment_date = models.DateTimeField(blank=True, null=True)
	rebill_status = models.CharField(max_length=10, blank=True, null=True, choices=REBILL_STATUS_CHOICES)
	rebill_frequency = models.CharField(max_length=20, blank=True, null=True)

	# Customer Fields
	full_name = models.CharField(max_length=510)
	first_name = models.CharField(max_length=255, blank=True, null=True)
	last_name = models.CharField(max_length=255, blank=True, null=True)
	province = models.CharField(max_length=2, blank=True, null=True)
	postal_code = models.CharField(max_length=16, blank=True, null=True)
	city = models.CharField(max_length=255, blank=True, null=True)
	country = models.CharField(max_length=255, blank=True, null=True)
	country_code = models.CharField(max_length=2, blank=True, null=True)
	email = models.CharField(max_length=255)
	address1 = models.CharField(max_length=255, blank=True, null=True)
	address2 = models.CharField(max_length=255, blank=True, null=True)

	# Shipping Fields
	shipping_address1 = models.CharField(max_length=255, blank=True, null=True)
	shipping_address2 = models.CharField(max_length=255, blank=True, null=True)
	shipping_city = models.CharField(max_length=255, blank=True, null=True)
	shipping_county = models.CharField(max_length=255, blank=True, null=True)
	shipping_province = models.CharField(max_length=255, blank=True, null=True)
	shipping_postal_code = models.CharField(max_length=255, blank=True, null=True)
	shipping_country = models.CharField(max_length=255, blank=True, null=True)
	shipping_amount = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)

	class Meta:
		verbose_name = u'notification'
		verbose_name_plural  = u'notifications'

	def initialize(self, request):
		""" If notification is being added from an actual Post this will set sender IP and store query if neccesary """
		if CLICKBANK_DEBUG or CLICKBANK_STORE_POSTS:
			post = Post(post_data=request.POST, get_data=request.GET)
			post.save()
			self.post_data = post
		self.sender_ip = request.META.get('REMOTE_ADDR', '')

	def send_signals(self):
		""" Send out neccesary signals on post_save or update """
		pass

	def __unicode__(self):
		return u'{0}'.format(self.receipt)