from django.urls import path
from . import views

urlpatterns = [
    # Endpoint for listing posts and creating new posts
    path('posts/', views.post_list_create_view, name='post-list-create'),
    
    # Endpoint for getting details of a specific post
    path('posts/<int:post_id>/', views.post_detail_view, name='post-detail'),
    
    # Endpoint for giving a star to a post
    path('posts/<int:post_id>/star/', views.give_star_view, name='give-star'),
]
