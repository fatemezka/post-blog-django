from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import LogoutView, LoginView

from users import views as user_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),

    path('register/', user_views.register, name='register'),
    path('login/', LoginView.as_view(template_name="users/login.html"), name='login'),
    path('logout/', LogoutView.as_view(template_name="users/logout.html"), name='logout'),
    path('profile/<str:username>/', user_views.profile, name='profile'),

]
