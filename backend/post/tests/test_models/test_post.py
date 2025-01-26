from django.test import TestCase
from post.tests.factory.post_factory import PostFactory
from post.models.post import Post

class TestPost(TestCase):
    def setUp(self):
        self.post = PostFactory()

    def test_post_creation(self):
        self.assertIsInstance(self.post, Post)
        self.assertIsNotNone(self.post.id)
        self.assertIsNotNone(self.post.created)
        self.assertIsNotNone(self.post.updated)
        self.assertIsNotNone(self.post.name)
        self.assertIsNotNone(self.post.description)
        self.assertTrue(self.post.status)

    def test_post_fields_types(self):
        self.assertIsInstance(self.post.name, str)
        self.assertIsInstance(self.post.description, str)
        self.assertIsInstance(self.post.status, bool)
