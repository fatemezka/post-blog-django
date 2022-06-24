from django.urls import path

from .views import *

app_name = 'blog'

urlpatterns = [

    path('', PostListView.as_view(), name='blog-home'),
    path('<str:username>/posts/', UserPostListView.as_view(), name='user-posts'),
    path('five-latest-posts/', FiveLatestPostListView.as_view(), name='five-latest-posts'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('about/', about_page, name='blog-about'),

]
