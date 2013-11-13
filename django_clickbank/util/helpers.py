import hashlib
import datetime
import time
import logging
import random
import string

from django.conf import settings
from django_clickbank.models import Notification

logger = logging.getLogger('django_clickbank.notifications')


def verify_secret(post, secret_key=settings.CLICKBANK_SECRET_KEY):
	""" Checks the secret key and makes sure the post hash matches """
	post = post.copy()
	try:
		post_hash = post.pop('cverify')
		if isinstance(post_hash, list):
			post_hash = post_hash[0]
		ipn_fields = []
		for key in post.keys():
			ipn_fields.append(key)
		ipn_fields.sort()

		data = []
		for field in ipn_fields:
			if isinstance(post[field], list):
				data.append(post[field][0])
			else:
				data.append(post[field])
		data.append(secret_key)
		hash_string = '|'.join(data)
		hex_digest = unicode(hashlib.sha1(hash_string).hexdigest()[:8].upper(), encoding='ascii')
		verification = post_hash == hex_digest
		#zimport ipdb; ipdb.set_trace()
		logger.debug('Verification: cverify = {0}'.format(repr(post_hash)))
		logger.debug('Verification: computed digest = {0}'.format(repr(hex_digest)))
		logger.debug('Verification: SECRET_KEY = {0}'.format(secret_key))
		logger.debug('Verification: Hashed String = {0}'.format(hash_string))
		logger.debug('Verification: {0}'.format(verification))

		return verification
	except Exception, e:
		raise
		logger.debug('Notification Verification Failed {0}'.format(e))
		return False


def make_secret(post, secret_key=settings.CLICKBANK_SECRET_KEY):
	""" Makes a new cverify from post parameters. Only usefull for creating test POSTs """

	post = post.copy()
	if 'cverify' in post:
		post_hash = post.pop('cverify')
	ipn_fields = []
	for key in post.keys():
		ipn_fields.append(key)
	ipn_fields.sort()

	data = []
	for field in ipn_fields:
		if isinstance(post[field], list):
			data.append(post[field][0])
		else:
			data.append(post[field])
	data.append(secret_key)
	hash_string = '|'.join(data)
	return hashlib.sha1(hash_string).hexdigest()[:8].upper()


class conditional_decorator(object):
	"""
	Used to apply a decorator based on a condition
	Condition can be either a function or Logic (IE. bool == False)
	Based on:
	http://stackoverflow.com/questions/10724854/how-to-do-a-conditional-decorator-in-python-2-6
	"""
	def __init__(self, decorator, condition):
		self.decorator = decorator
		self.condition = condition

	def __call__(self, function):
		if not self.condition:
			# Do nothing
			return function
		return self.decorator(function)


def remap_post(data):
	"""
	Remaps a dictionary to use new keys as defined below.
	Used to get around the fact that clickbank uses post_data with names
	that don't fit well with python/django naming conventions.
	"""
	remapped_data = {}
	MAPPING = {
		u'caccountamount': u'recieved_amount',
		u'cnoticeversion': u'notification_version',
		u'cbf': u'upsell_flow',
		u'ctranspaymentmethod': u'payment_method',
		u'corderamount': u'order_amount',
		u'ctaxamount': u'tax_amount',
		u'ccustzip': u'postal_code',
		u'ctransreceipt': u'receipt',
		u'ccustfullname': u'full_name',
		u'ctid': u'tracking_id',
		u'corderlanguage': u'order_language',
		u'ccustcounty': u'country',
		u'ccustcc': u'country_code',
		u'ccuststate': u'province',
		u'cfuturepayments': u'future_payments',
		u'crebillamnt': u'rebill_amount',
		u'ccustaddr2': u'shipping_address2',
		u'cshippingamount': u'shipping_amount',
		u'ctransaction': u'transaction_type',
		u'ctransvendor': u'transaction_vendor',
		u'ccustshippingzip': u'shipping_postal_code',
		u'ctransaffiliate': u'transaction_affiliate',
		u'ccustemail': u'email',
		u'cupsellreceipt': u'parent_receipt',
		u'cprodtitle': u'product_title',
		u'ctransrole': u'role',
		u'crebillstatus': u'rebill_status',
		u'cvendthru': u'extra_data',
		u'cprodtype': u'product_type',
		u'ccustfirstname': u'first_name',
		u'ctranstime': u'transaction_date',
		u'ccurrency': u'currency',
		u'cprocessedpayments': u'processed_payments',
		u'ccustshippingcountry': u'shipping_country',
		u'ccustlastname': u'last_name',
		u'cnextpaymentdate': u'next_payment_date',
		u'cproditem': u'product_id',
		u'ccustaddr1': u'address1',
		u'ccustaddr2': u'address2',
		u'ccustcity': u'city',
		u'crebillfrequency': u'rebill_frequency',
		u'ccustshippingstate': u'shipping_province'
	}

	for key, value in data.iteritems():
		if key in MAPPING:
			remapped_data[MAPPING[key]] = value

	return remapped_data


def epoch_to_datetime(epochtime):
	""" Converts a unix epoch time to python datetime """
	return datetime.datetime.utcfromtimestamp(int(epochtime))


def date_to_datetime(date):
	""" Convert Clickbank date data (YEAR-MONTH-DAY) to datetime """
	return datetime.datetime.strptime(date, '%Y-%m-%d').date()


def cents_to_decimal(cents):
	""" Used to turns clickbank amounts (in cents) to decimal number """
	if cents:
		return float(cents) / 100


def amount_generator(min=200, max=999999):
	""" Used to generate a random amount in cents """
	return str(random.randrange(min, max))


def receipt_generator():
	""" Used to generate a random receipt for testing """
	return ''.join(random.choice(string.ascii_uppercase + string.digits) for x in range(13))


def zip_generator():
	""" Generate a string similar to that of a U.S. Zip code """
	return str(random.randrange(00000, 99999))


def string_generator(length=5, chars=string.ascii_uppercase + string.digits):
	""" Generate a string. Defaults to uppercase ASCII and numbers """
	return ''.join(random.choice(chars) for x in range(length))


def language_generator():
	""" Grab a random language from django languages dict """
	from django.conf.global_settings import LANGUAGES
	return random.choice(LANGUAGES)[0].upper()


def future_epock_generator(min_days=2, max_days=30):
	""" Get a random future epoch datetime. Default 2-30 days in the future """
	now = datetime.datetime.now()
	timedelta = datetime.timedelta(days=random.randrange(min_days, max_days))
	return str(int(time.mktime((now + timedelta).timetuple())))


def future_date_generator(min_days=2, max_days=30):
	""" Get a random future date string. Default 2-30 days in the future """
	now = datetime.datetime.now()
	timedelta = datetime.timedelta(days=random.randrange(min_days, max_days))
	return (now + timedelta).strftime('%Y-%m-%d')


def generate_post(secret_key=settings.CLICKBANK_SECRET_KEY, data=None):
	""" Generate a post with a given secret key for use with testing """
	import names
	first_name = names.get_first_name()
	last_name = names.get_last_name()

	post_data = {
		u'caccountamount': amount_generator(),
		u'cnoticeversion': u'4.0',
		u'cbf': u'',
		u'ctranspaymentmethod': random.choice(Notification.PAYMENT_METHOD_CHOICES)[0],
		u'corderamount': amount_generator(),
		u'ctaxamount': amount_generator(),
		u'ccustzip': zip_generator(),
		u'ctransreceipt': receipt_generator(),
		u'ccustfullname': ' '.join([first_name, last_name]),
		u'ctid': string_generator(),
		u'corderlanguage': language_generator(),
		u'ccustcounty': string_generator(),
		u'ccustcc': string_generator(2),
		u'ccuststate': string_generator(2),
		u'cbfpath': u'',
		u'cfuturepayments': string_generator(length=1, chars=string.digits),
		u'crebillamnt': amount_generator(),
		u'ccustaddr2': string_generator(20),
		u'cshippingamount': amount_generator(),
		u'ctransaction': random.choice(Notification.TRANSACTION_TYPE_CHOICES)[0],
		u'ctransvendor': string_generator(),
		u'ccustshippingzip': zip_generator(),
		u'ctransaffiliate': string_generator(),
		u'ccustemail': string_generator(),
		u'cupsellreceipt': receipt_generator(),
		u'cprodtitle': string_generator(),
		u'ctransrole': random.choice(Notification.ROLE_CHOICES)[0],
		u'crebillstatus': random.choice(Notification.REBILL_STATUS_CHOICES)[0],
		u'cbfid': u'',
		u'cvendthru': u'',
		u'cprodtype': random.choice(Notification.PRODUCT_TYPE_CHOICES)[0],
		u'ccustfirstname': first_name,
		u'ctranstime': u'1383333571',
		u'ccurrency': string_generator(chars=string.ascii_uppercase, length=3)[0],
		u'cprocessedpayments': str(random.randrange(1, 100)),
		u'ccustshippingcountry': string_generator(),
		u'ccustlastname': last_name,
		u'cnextpaymentdate': future_date_generator(),
		u'cproditem': string_generator(chars=string.digits),
		u'ccustaddr1': string_generator(length=20),
		u'ccustcity': string_generator(length=10),
		u'crebillfrequency': u'',
		u'ccustshippingstate': string_generator(length=2, chars=string.ascii_uppercase)
	}
	post_data[u'cverify'] = make_secret(post_data)
	return post_data
