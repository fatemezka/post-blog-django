from django.urls import path

from .views import *


app_name = 'blog'

urlpatterns = [

    # path('', PostList.as_view(), name='blog-home'),
    path('', HomePage.as_view(), name='blog-home'),
    path('about/',about_page, name='blog-about'),

]
