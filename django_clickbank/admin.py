from django.contrib import admin
from django_clickbank.models import Notification, Post
from django_clickbank.forms import PostAdminForm


class NotificationAdmin(admin.ModelAdmin):

	model = Notification

	list_display = ['receipt', 'parent_receipt', 'transaction_type', 'email', 'product_title',
	'product_type', 'order_amount', 'recieved_amount', 'transaction_affiliate', 'transaction_date']

	readonly_fields = ['post_data']


class PostAdmin(admin.ModelAdmin):

	model = Post
	form = PostAdminForm
	list_display = ['id', 'time', ]
	list_display_links = list_display


admin.site.register(Notification, NotificationAdmin)
admin.site.register(Post, PostAdmin)
