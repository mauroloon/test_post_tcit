from django.test import TestCase
from uuid import uuid4
from django.urls import reverse
from rest_framework.test import APIClient
from post.models import Post
from rest_framework import status
from post.tests.factory.post_factory import PostFactory

class TestPostView(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.post = PostFactory(
            name="Test Post",
            description="Test Description",
        )

    def test_get_posts(self):
        url = reverse('get_posts')
        response = self.client.get(url)
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['name'], self.post.name)

    def test_create_post(self):
        url = reverse('create_post')
        data = {
            'name': 'New Post',
            'description': 'New Description'
        }
        
        response = self.client.post(url, data, format='json')
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], data['name'])
        self.assertEqual(response.data['description'], data['description'])
        self.assertTrue(Post.objects.filter(name=data['name']).exists())

    def test_delete_post(self):
        url = reverse('delete_post', kwargs={'id': self.post.id})
        response = self.client.delete(url)
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(str(response.data['id']), str(self.post.id))  # Convertimos UUID a string
        self.assertEqual(Post.objects.filter(status=True).count(), 0)

    def test_delete_post_not_found(self):
        
        url = reverse('delete_post', kwargs={'id': uuid4()})
        response = self.client.delete(url)
        
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
