from django.conf import settings

class ClickBankSettingsException(Exception):
	""" Raised when a django-clickbank setting is missing or incorrect """


try:
	CLICKBANK_SECRET_KEY = getattr(settings, 'CLICKBANK_SECRET_KEY')
except AttributeError, e:
	raise ClickBankSettingsException(e)

## Setting debug to True turns off things like secret key verification
CLICKBANK_DEBUG = getattr(settings, 'CLICKBANK_DEBUG', False)

## If set to true raw post data will be stored regardless of CLICKBANK_DEBUG
CLICKBANK_STORE_POSTS = getattr(settings, 'CLICKBANK_STORE_POSTS', True)

## If set to true, app will still log notifications when verification fails
CLICKBANK_KEEP_INVALID = getattr(settings, 'CLICKBANK_KEEP_INVALID', True)

## When set to true, app will still send signal when invalid notification recieved.
CLICKBANK_SIGNAL_INVALID = getattr(settings, 'CLICKBANK_SIGNAL_INVALID', False)