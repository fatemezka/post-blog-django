from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import LogoutView, LoginView


from django.conf import settings
from django.conf.urls.static import static


from users import views as user_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),

    path('register/', user_views.register, name='register'),
    path('login/', LoginView.as_view(template_name="users/login.html"), name='login'),
    path('logout/', LogoutView.as_view(template_name="users/logout.html"), name='logout'),
    path('profile/<str:username>/', user_views.profile, name='profile'),

]

if settings.DEBUG: # It means if we are currently in DEBUG mode.
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
