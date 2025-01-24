from post.views.post_view import PostServices
from django.urls import path

urlpatterns = [
    path('posts', PostServices.as_view(), name='get_posts'),
    path('posts/create', PostServices.as_view(), name='create_post'),
    path('posts/<str:id>', PostServices.as_view(), name='delete_post'),
]