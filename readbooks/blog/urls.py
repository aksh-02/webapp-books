from django.urls import path
from .views import add_post, view_post, posts_home, DeletePost, UpdatePost, UserPostView

urlpatterns = [
    path('', posts_home, name='posts-home'),
    path('post', add_post, name='add-post'),
    path('post/<str:slug>', view_post, name='view-post'),
    path('post/<str:slug>/delete', DeletePost.as_view(), name='delete-post'),
    path('post/<str:slug>/update', UpdatePost.as_view(), name='update-post'),
    path('user/<str:username>', UserPostView.as_view(), name='user-post'),
]