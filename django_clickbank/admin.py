from django.contrib import admin
from django_clickbank.models import Notification, Post
from django_clickbank.forms import PostAdminForm
from django.conf import settings


class NotificationAdmin(admin.ModelAdmin):

	model = Notification

	list_display = ['receipt', 'parent_receipt', 'transaction_type', 'email', 'product_title',
	'product_type', 'order_amount', 'recieved_amount', 'transaction_affiliate', 'transaction_date']
	list_filter = ['transaction_type', 'transaction_date', 'verification_passed']
	readonly_fields = ['post_data']
	search_fields = ['receipt', 'parent_receipt', 'email', 'full_name', 'transaction_affiliate']

	def resend_signals(self, request, queryset):
		"""
		Resend signals for notifications. This should probably only be used to debug
		your application.
		"""
		for notification in queryset:
			notification.send_signals()

	resend_signals.short_description = 'Resend django signals for selected notifications'

	if settings.CLICKBANK_RESEND_SIGNALS:
		actions = [resend_signals]


class PostAdmin(admin.ModelAdmin):

	model = Post
	form = PostAdminForm
	list_display = ['id', 'time', ]
	list_display_links = list_display
	list_filter = ['failed',]


admin.site.register(Notification, NotificationAdmin)
admin.site.register(Post, PostAdmin)
