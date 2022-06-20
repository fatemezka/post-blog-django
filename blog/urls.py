from django.urls import path

from .views import *

urlpatterns = [

    path('', PostList.as_view(), name='blog-home'),
    path('about/',about_page, name='blog-about'),

]
