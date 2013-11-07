from .settings import CLICKBANK_SECRET_KEY, CLICKBANK_DEBUG
import hashlib
from .exceptions import NotificationFailedValidation
import datetime
import logging
logger = logging.getLogger('django_clickbank.notifications')

def verify_secret(post, secret_key = None):
	""" Checks the secret key and makes sure the post hash matches """
	if secret_key is None:
		secret_key = CLICKBANK_SECRET_KEY
	post = post.copy()
	try:
		post_hash = post.pop('cverify')
		ipn_fields = []
		for key in post.keys():
			ipn_fields.append(key)
		ipn_fields.sort()
		
		data = []
		for field in ipn_fields:
			data.append(post[field])
		data.append(secret_key)
		hash_string = '|'.join(data)
		return post_hash == hashlib.sha1(hash_string).hexdigest()[:8].upper()
	except Exception, e:
		logger.debug('Notification Verification Failed {0}'.format(e))
		return False

def make_secret(post, secret_key = None):
	""" Makes a new cverify from post parameters. Only usefull for creating test POSTs """

	if secret_key is None:
		secret_key = CLICKBANK_SECRET_KEY
	post = post.copy()
	if 'cverify' in post:
		post_hash = post.pop('cverify')
	ipn_fields = []
	for key in post.keys():
		ipn_fields.append(key)
	ipn_fields.sort()
	
	data = []
	for field in ipn_fields:
		data.append(post[field])
	data.append(secret_key)
	hash_string = '|'.join(data)
	return hashlib.sha1(hash_string).hexdigest()[:8].upper()


class conditional_decorator(object):
	""" 
	Used to apply a decorator based on a condition
	Condition can be either a function or Logic (IE. bool == False)
	Based on http://stackoverflow.com/questions/10724854/how-to-do-a-conditional-decorator-in-python-2-6
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


def generate_post(secret_key=CLICKBANK_SECRET_KEY, data=None):
	""" Generate a post with a given secret key for use with testing """
	pass