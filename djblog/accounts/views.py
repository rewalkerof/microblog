from django.contrib.auth import (
    authenticate,
    get_user_model,
    login, logout
)
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse

from .forms import UserLoginForm


def account_login(request):
    form = UserLoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return redirect('posts:list')
    context = {
        'title': "Log in",
        'form': form,
    }
    return render(request, 'accounts/login.html', context)


# def account_register(request):
#     return render(request)
#

def account_logout(request):
    logout(request)
    return redirect('posts:list')
