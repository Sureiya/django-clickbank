from django import forms
from django_clickbank.models import Notification, Post


class NotificationForm(forms.ModelForm):
	""" Form used to recieve and validate ClickBank IPN Data """

	class Meta:
		model = Notification


class PostAdminForm(forms.ModelForm):
	post_data = forms.CharField(widget=forms.Textarea)
	get_data = forms.CharField(widget=forms.Textarea)

	class Meta:
		model = Post
