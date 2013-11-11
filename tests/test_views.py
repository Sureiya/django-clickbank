from django.core.urlresolvers import reverse
from django.test import TestCase, Client
from django.test.utils import  override_settings
from django_clickbank.models import Post, Notification
from django_clickbank.tests.posts import TEST_POSTS, SECRET_KEY
from django_clickbank.util.helpers import generate_post
from django.conf import settings
import simplejson as json

@override_settings(CLICKBANK_SECRET_KEY=SECRET_KEY)
class ViewTest(TestCase):

	def test_debug_ipn(self):
		client = Client()
		for post in TEST_POSTS:
			response = client.post(reverse('clickbank.debug.ipn_data'), post)
			self.assertEqual(response.status_code, 200)
			post= Post.objects.get(pk=int(response.content))
			self.assertIsInstance(post, Post)
			self.assertNotEqual(post.post_data, '')
			self.assertNotEqual(post.post_data, None)

	def test_ipn(self):
		client = Client()
		import copy
		test_posts = copy.deepcopy(TEST_POSTS)
		for i in range(0, 100):
			test_posts.append(generate_post(SECRET_KEY))

		for post in test_posts:
			response = client.post(reverse('clickbank.ipn'), post)
			self.assertEqual(response.status_code, 200)
			notification = Notification.objects.get(pk=int(response.content))
			self.assertIsInstance(notification, Notification)
			self.assertTrue(notification.verification_passed)
