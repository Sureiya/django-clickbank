from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
import simplejson as json
import logging

from .models import Post
from .forms import NotificationForm
from .settings import *
from .helpers import conditional_decorator, verify_secret, remap_post, epoch_to_datetime
from .exceptions import NotificationFailedValidation

logger = logging.getLogger('django_clickbank.notifications')

DATE_FIELDS = (
	'transaction_date',
	)

@csrf_exempt
def record_ipn_data(request):
	post = Post(post_data=json.dumps(request.POST), get_data=json.dumps(request.GET))
	post.save()
	return HttpResponse(post.id, status=200)


@conditional_decorator(require_POST, CLICKBANK_DEBUG == False)
@csrf_exempt
def ipn(request, get=False):
	## Copy data. Get copying is for debug mode.
	if get:
		data = request.GET.copy()
	else:
		data = request.POST.copy()

	logger.debug('Notifaction Received: {0}'.format(json.dumps(data)))

	# Verify cverify and potentially output error based on settings.
	if not verify_secret(data):
		logger.debug('Verification Failed')
		verification = False
		if not CLICKBANK_KEEP_INVALID:
			raise NotificationFailedValidation('Verification Failed and CLICKBANK_KEEP_INVALID is False')
	else:
		verification = True
		logger.debug('Verification Passed')

	# Remap ugly clickbank field names to match django model field names
	mapped_data = remap_post(data)

	# Clickbank sends times as epoch times which aren't very usefull to us, so lets fix them.
	for field in DATE_FIELDS:
		if field in mapped_data:
			mapped_data[field] = epoch_to_datetime(mapped_data[field])

	form = NotificationForm(mapped_data)
	if form.is_valid():
		try:
			notification = form.save(commit = False)
		except Exception, e:
			raise NotificationFailedValidation(e)
	else: 
		raise NotificationFailedValidation(form.errors)

	notification.initialize(request)
	notification.save()

	return HttpResponse(form)