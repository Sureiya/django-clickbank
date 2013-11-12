from django.conf.urls import patterns, url

urlpatterns = patterns('',
	url(r'^ipn/$', 'django_clickbank.views.ipn', name='clickbank.ipn'),
	url(r'^ipn/get/$', 'django_clickbank.views.ipn', {'get': True}, name='clickbank.ipn.get'),
)
