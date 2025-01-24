import uuid
from django.db import models

class BaseModel(models.Model):
    """
    Modelo base para los modelos de la aplicación

    Attributes:
        id (UUID): Id del modelo
        created (DateTime): Fecha de creación del modelo
        updated (DateTime): Fecha de actualización del modelo
        status (Boolean): Estado del modelo

    Meta:
        abstract (bool): Indica que este modelo no es una tabla en la base de datos
    """


    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    class Meta:
        abstract = True