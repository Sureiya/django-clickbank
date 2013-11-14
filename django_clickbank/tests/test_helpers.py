from django.test import TestCase
from django_clickbank.tests.posts import TEST_POSTS, SECRET_KEY
from django_clickbank import settings
from django_clickbank.util.helpers import remap_post
from django_clickbank.util.helpers import generate_post


class HelperTest(TestCase):
	def setUp(self):
		settings.CLICKBANK_SECRET_KEY = SECRET_KEY

	def test_ipn_verify(self):
		from django_clickbank.util.helpers import verify_secret as verify

		for post in TEST_POSTS:
			self.assertTrue(verify(post, SECRET_KEY))

	def test_remap_post(self):

		import copy
		test_posts = copy.deepcopy(TEST_POSTS)

		for i in range(0, 25):
			test_posts.append(generate_post(SECRET_KEY))

		for post in TEST_POSTS:
			self.assertGreater(len(remap_post(post)), 30)
