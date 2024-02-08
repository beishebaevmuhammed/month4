from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

from users.forms import RegisterForm, LoginForm, UserProfileForm


# Create your views here.

def register_view(request):
    context = {
            'form': RegisterForm()
        }
    if request.method == 'GET':
        return render(request, 'users/register.html', context)
    elif request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            User.objects.create_user(**form.cleaned_data)
            return redirect('/login/')
        else:
            return render(request, 'users/register.html', context)


def login_view(request):
    context = {
        'form': LoginForm()
    }
    if request.method == 'GET':
        return render(request, 'users/login.html', context)
    elif request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(**form.cleaned_data)
            if user is not None:
                login(request, user)
                return redirect('/products/')
            else:
                form.add_error('username', 'Такого пользователя не существует!')
        else:
            return render(request, 'users/login.html', context)

def logout_view(request):
    logout(request)
    return redirect('/products/')

def profile_view(request):
    if request.method == 'GET':
        return render(request, 'users/profile.html', {"user": request.user})


def profile_update_view(request):
    user_profile = request.user

    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=user_profile)
        if form.is_valid():
            form.save()
            return redirect('/profile/')
    else:
        form = UserProfileForm(instance=user_profile)

    return render(request, 'users/profile_update.html', {"form": form})



