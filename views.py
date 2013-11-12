from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.conf import settings

try:
	import simplejson as json
except:
	import json

import logging

from django_clickbank.models import Post, Notification
from django_clickbank.forms import NotificationForm
from django_clickbank.util.helpers import conditional_decorator, verify_secret, remap_post,\
																		epoch_to_datetime, date_to_datetime
from django_clickbank.util.helpers import cents_to_decimal
from django_clickbank.util.exceptions import NotificationFailedValidation

logger = logging.getLogger('django_clickbank.notifications')


@conditional_decorator(require_POST, settings.CLICKBANK_DEBUG is False)
@csrf_exempt
def ipn(request, get=False):
	"""
	IPN View. If CLICKBANK_DEBUG == True then you can use the url /ipn/get/ to post
	to it using get requests. This is usefull for testing without using a REST Client or cURL
	"""
	## Copy data. GET copying is for debug mode.
	try:
		if get:
			data = request.GET.copy()
		else:
			data = request.POST.copy()

		logger.debug('Notifaction Received: {0}'.format(json.dumps(data)))

		# Verify cverify and potentially output error based on settings.
		if not verify_secret(data):
			logger.debug('Verification Failed')
			verification = False
			if not settings.CLICKBANK_KEEP_INVALID:
				raise NotificationFailedValidation(
					'Verification Failed and CLICKBANK_KEEP_INVALID is False')
		else:
			verification = True
			logger.debug('Verification Passed')

		# Remap ugly clickbank field names to match django model field names
		mapped_data = remap_post(data)

		# Clickbank sends times as epoch times which aren't very usefull to us, so lets fix them.
		for field in Notification.TIME_FIELDS:
			if field in mapped_data:
				if mapped_data[field]:
					mapped_data[field] = epoch_to_datetime(mapped_data[field])

		for field in Notification.DATE_FIELDS:
			if field in mapped_data:
				if mapped_data[field]:
					mapped_data[field] = date_to_datetime(mapped_data[field])

		# Some Clickbank Fields are stored in
		# Lets store those cent amount as decimal number to make it easier to work with.
		for field in Notification.AMOUNT_FIELDS:
			if field in mapped_data:
				if mapped_data[field]:
					mapped_data[field] = cents_to_decimal(mapped_data[field])

		# New form instanced with newly mapped data
		form = NotificationForm(mapped_data)
		if form.is_valid():
			try:
				# Create a new notification instance, but don't save it.
				# We want to be able to do more with it before the post_create and post_save signals
				# are called.
				notification = form.save(commit=False)
			except Exception, e:
				raise NotificationFailedValidation(e)
		else:
			raise NotificationFailedValidation('{0}\n{1}\n{2}'.format(form.errors, mapped_data, data))

		notification.initialize(request)
		notification.verification_passed = verification
		notification.save()

		logger.info('Notification Processed Succesfully:')
		logger.info('Source: {0} Receipt: {1} Type: {2} Vendor: {3} Affiliate: {4} Product: {5}'.format(
			notification.sender_ip, notification.receipt, notification.transaction_type,
			notification.transaction_vendor, notification.transaction_affiliate,
			'{0}:{1}'.format(notification.product_id, notification.product_title)))

		return HttpResponse(notification.id)
	except:
		post = Post(get_data=request.GET, post_data=request.POST, failed=True)
		post.save()
		raise
