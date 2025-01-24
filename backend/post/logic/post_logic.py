from typing import Optional
from post.models import Post
from django.db.models import QuerySet


class PostLogic:

    @staticmethod
    def get_all_posts_active() -> QuerySet:
        """
        Obtiene todos los posts activos

        Returns:
            QuerySet: QuerySet de los posts activos
        """
        return Post.objects.filter(status=True)
        
    @staticmethod
    def get_post_by_name(name: str) -> Optional[Post]:
        """
        Obtiene un post por su nombre

        args:
            name (str): Nombre del post

        Returns:
            Optional[Post]: Post encontrado o None
        """
        try:
            return Post.objects.get(name=name)
        except Post.DoesNotExist:
            return None
    
    @staticmethod
    def create_post(name: str, description: str) -> Post:
        """
        Crea un post

        args:
            name (str): Nombre del post
            description (str): Descripción del post

        Returns:
            Post: Post creado
        """
        post = Post(name=name, description=description)
        post.save()
        return post
    
    @staticmethod
    def delete_post(id: str) -> Optional[Post]:
        """
        Deshabilita un post si está activo
        # No elimino datos a menos que sea muy necesario

        args:
            id (str): Id del post

        Returns:
            Optional[Post]: Post Deshabilitado o None
        """
        post = Post.objects.filter(id=id, status=True).first()

        if not post:
            return None
        
        post.status = False
        post.save()
        return post
