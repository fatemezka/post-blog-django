from django.shortcuts import render, redirect
# from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages

from .forms import UserRegisterForm


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=True)
            messages.success(request, f"Account created for [{user.username}].")
            login(request, user)
            return redirect('blog:blog-home')



    else:
        form = UserRegisterForm()

    context = {'form': form}
    return render(request, 'users/register.html', context)

@login_required(login_url='login')
def profile(request, username):
    user = User.objects.get(username=username)
    return render(request, 'users/profile.html', {'user': user})
