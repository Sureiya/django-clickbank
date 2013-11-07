from django.test import TestCase
from .posts import TEST_POSTS, SECRET_KEY

class HelperTest(TestCase):

	def test_ipn_verify(self):
		from ..helpers import verify_secret as verify

		for post in TEST_POSTS:
			self.assertTrue(verify(post, SECRET_KEY))

	def test_remap_post(self):
		from ..helpers import remap_post

		for post in TEST_POSTS:
			self.assertGreater(len(remap_post(post)), 30)