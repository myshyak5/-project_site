from django.shortcuts import render, redirect
from django.contrib import auth, messages
from django.urls import reverse
from django.http import HttpResponseRedirect
from .forms import UserLoginForm, UserRegistrationForm, ProfileForm
from django.contrib.auth.decorators import login_required


def login(request):
    if request.user.is_authenticated:
        return redirect(reverse('users:profile'))
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user:
                auth.login(request, user)
                return HttpResponseRedirect(reverse('main:product_list'))
    else:
        form = UserLoginForm()
    return render(request, 'users/login.html', {'form': form})

def registration(request):
    if request.method == 'POST':
        form = UserRegistrationForm(data=request.POST)
        if form.is_valid():
            form.save()
            user = form.instance
            auth.login(request, user)
            messages.success(request, f'{user.username}, successful registration!')
            return HttpResponseRedirect(reverse('users:login'))
    else:
        form = UserRegistrationForm()
    return render(request, 'users/registration.html', {'form': form})

@login_required(login_url='/user/login/')
def profile(request):
    if request.method == 'POST':
        form = ProfileForm(data=request.POST, instance=request.user,
                           files=request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile was changed')
            return HttpResponseRedirect(reverse('users:profile'))
    else:
        form = ProfileForm(instance=request.user)
    return render(request, 'users/profile.html', {'form': form})

def logout(request):
    auth.logout(request)
    return redirect(reverse('main:index_list'))