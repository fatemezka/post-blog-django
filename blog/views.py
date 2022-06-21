from django.shortcuts import render
from django.views.generic import ListView, DetailView, UpdateView, DeleteView


from .models import Post


def about_page(request):
    return render(request,'blog/about.html')

class HomePage(ListView):
    model = Post
    template_name = 'blog/home_page.html'
    context_object_name = 'posts'


# def home_page(request):
#     posts = Post.objects.all()
#     context = {'posts':posts}
#     if request.user.is_authenticated:
#         context['username']=request.user.username
#     return render(request,'blog/home_page.html',context)