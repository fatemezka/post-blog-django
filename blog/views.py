from django.shortcuts import render
from django.views.generic import ListView, DetailView, UpdateView, DeleteView


from .models import Post


def about_page(request):
    return render(request,'blog/about.html')

class PostList(ListView):
    model = Post
    template_name = 'blog/home_page.html'
    context_object_name = 'posts'

