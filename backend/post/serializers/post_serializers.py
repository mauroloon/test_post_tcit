from rest_framework import serializers
from post.models import Post

class PostSerializer(serializers.ModelSerializer):
    """
    Serializador de Post

    Attributes:
        id (UUID): Id del post
        name (str): Nombre del post
        description (str): Descripción del post
    """


    class Meta:
        model = Post
        fields = ['id', 'name', 'description']
