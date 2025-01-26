import factory
import uuid
from django.utils import timezone

from post.models.post import Post

class PostFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Post
    
    id = factory.LazyFunction(uuid.uuid4)
    created = factory.LazyFunction(timezone.now)
    updated = factory.LazyFunction(timezone.now)
    name = factory.Faker('sentence', nb_words=3)
    description = factory.Faker('text', max_nb_chars=400)
    status = True

