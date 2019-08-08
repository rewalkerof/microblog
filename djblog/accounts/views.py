from django.contrib.auth import (
    authenticate,
    get_user_model,
    login, logout
)
from django.shortcuts import render, redirect

from .forms import UserLoginForm, UserRegisterForm


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


def account_register(request):
    form = UserRegisterForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        username = form.cleaned_data.get('username')
        email = form.cleaned_data.get('email')
        password = form.cleaned_data.get('password')
        user.set_password(password)
        user.save()
        new_user = authenticate(username=user.username, password=password)
        login(request, new_user)
        return redirect('posts:list')
    context = {
        'title': 'Register',
        'form': form,
    }
    return render(request, 'accounts/register.html', context)


def account_logout(request):
    logout(request)
    return redirect('accounts:login')
