from post.models.base_model import BaseModel
from django.db import models


class Post(BaseModel):
    """
    Modelo de Post

    Attributes:
        name (str): Nombre del post
        description (str): Descripción del post

    Meta:
        db_table (str): Nombre de la tabla en la base de datos
        ordering (list): Ordenamiento
    """
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=500)

    class Meta:
        db_table = 'post'
        ordering = ['-created']