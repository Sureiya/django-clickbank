from setuptools import setup, find_packages
import django_clickbank

setup(
	name = "django-clickbank",
	version = django_clickbank.__version__,
	packages = find_packages(),

	author = "Chris Modjeska",
	author_email = "kin@remuria.net",
	description = "A pluggable application for receiving data from ClickBank's Instant Payment Notifications",
	license = "MIT",
	keywords = "django clickbank ipn",
	url = "https://github.com/sureiya/django_clickbank/",
	include_package_data=True,

	classifiers=[
		"Framework :: Django",
		"Intended Audience :: Developers",
		"Intended Audience :: System Administrators",
		"Operating System :: OS Independent",
		"Topic :: Software Development"
	],
	long_description= """
	==============
	django-paypal
	==============
	django-paypal is a pluggable application for recieving ClickBank's Instant Payment
	Notifications. For more info please visit the github page at 
	https://github.com/sureiya/django-clickbank
	""",
)