#!/usr/bin/env python

from os.path import dirname, abspath
import sys

from django.conf import settings
from django.core.management import call_command
from django_clickbank import settings as django_clickbank_defaults

if not settings.configured:
	settings.configure(
		CLICKBANK_DEBUG=False,
		CLICKBANK_STORE_POSTS=True,
		CLICKBANK_KEEP_INVALID=True,
		CLICKBANK_SIGNAL_INVALID=False,
		CLICKBANK_IGNORE_DUPLICATES=False,
		CLICKBANK_SECRET_KEY='76AFC0778E648BDA05705047BAFA96ED',
		ROOT_URLCONF='django_clickbank.urls',
		DATABASES = {'default': {'ENGINE': 'django.db.backends.sqlite3','NAME': ':memory:',}},
		INSTALLED_APPS=[
			'django_clickbank',
			'django_nose',
		],
		TEST_RUNNER = 'django_nose.NoseTestSuiteRunner',
	)


def runtests(*test_args):
	parent = dirname(abspath(__file__))
	sys.path.insert(0, parent)
	
	output = call_command('test', verbosity=1, interactive=True)
	sys.exit(output)


if __name__ == '__main__':
	runtests()