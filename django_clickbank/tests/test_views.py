from django.core.urlresolvers import reverse
from django.test import TestCase, Client
from django.test.utils import override_settings
from django_clickbank.models import Post, Notification
from django_clickbank.tests.posts import TEST_POSTS, SECRET_KEY
from django_clickbank.util.helpers import generate_post


@override_settings(CLICKBANK_SECRET_KEY=SECRET_KEY)
class ViewTest(TestCase):

	def test_ipn(self):
		client = Client()
		import copy
		test_posts = copy.deepcopy(TEST_POSTS)
		for i in range(0, 10):
			test_posts.append(generate_post(SECRET_KEY))

		for post in test_posts:
			response = client.post(reverse('clickbank.ipn'), post)
			self.assertEqual(response.status_code, 200)
			notification = Notification.objects.get(pk=int(response.content))
			self.assertIsInstance(notification, Notification)
			self.assertTrue(notification.verification_passed)
