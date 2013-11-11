from django.conf.urls import patterns, url
from django.views.generic import TemplateView
from django_clickbank.views import record_ipn_data
from django.views.decorators.csrf import csrf_exempt

urlpatterns = patterns('',
	url(r'^debug_ipn/$', 'django_clickbank.views.record_ipn_data', name='clickbank.debug.ipn_data'),
	url(r'^ipn/$', 'django_clickbank.views.ipn', name='clickbank.ipn'),
	url(r'^ipn/get/$', 'django_clickbank.views.ipn', { 'get': True }, name='clickbank.ipn.get'),
)
