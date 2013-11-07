from django.core.urlresolvers import reverse
from django.test import TestCase, Client
from ..models import Post, Notification
from .posts import TEST_POSTS, SECRET_KEY
import simplejson as json

class ViewTest(TestCase):
	
	def test_debug_ipn(self):
		client = Client()
		for id, post in enumerate(TEST_POSTS):
			response = client.post(reverse('clickbank.debug.ipn_data'), post)
			self.assertEqual(response.status_code, 200)
			post_object = Post.objects.get(pk=int(response.content))
			self.assertIsInstance(post_object, Post)