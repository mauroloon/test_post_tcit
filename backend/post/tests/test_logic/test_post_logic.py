from django.test import TestCase
from post.logic.post_logic import PostLogic
from post.models import Post
from post.tests.factory.post_factory import PostFactory

class TestPostLogic(TestCase):
    def setUp(self):
        # Crear posts de prueba usando factory
        self.post1 = PostFactory(name="Test Post 1", description="Description 1")
        self.post2 = PostFactory(name="Test Post 2", description="Description 2")
        self.post_logic = PostLogic()

    def test_create_post(self):
        data = {"name": "New Post", "description": "New Description"}
        new_post = self.post_logic.create_post(name=data["name"], description=data["description"])
        self.assertEqual(new_post.name, "New Post")
        self.assertEqual(new_post.description, "New Description")

    def test_get_all_posts(self):
        # Prueba obtener todos los posts
        posts = self.post_logic.get_all_posts_active()
        self.assertEqual(len(posts), 2)

    def test_delete_post(self):
        # Prueba eliminar un post
        result = self.post_logic.delete_post(self.post1.id)
        self.assertEqual(result.status, False)

    def test_search_posts_by_name(self):
        # Prueba buscar posts por nombre usando factory
        PostFactory(name="Unique Post Name")
        posts = self.post_logic.get_post_by_name("Unique Post Name")
        self.assertEqual(posts.name, "Unique Post Name")

    def test_search_posts_empty_name(self):
        # Prueba buscar con nombre vacío
        posts = self.post_logic.get_post_by_name("")
        self.assertEqual(posts, None)

    def test_delete_nonexistent_post(self):
        # Prueba eliminar un post que no existe
        result = self.post_logic.delete_post(999)
        self.assertFalse(result)
