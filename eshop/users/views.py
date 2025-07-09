from django.shortcuts import render, redirect
from django.contrib import auth, messages
from django.urls import reverse
from django.http import HttpResponseRedirect
from .forms import UserLoginForm, UserRegistrationForm, ProfileForm
from django.contrib.auth.decorators import login_required


def login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user:
                auth.login(request, user)
                return HttpResponseRedirect(reverse('main:product'))
    else:
        form = UserLoginForm()
    # return render(request, 'users/login.html')
    return render(request, 'users/login.html', {'form': form})

def registration(request):
    if request.method == 'POST':
        form = UserRegistrationForm(data=request.POST)
        if form.is_valid():
            form.save()
            user = form.instance
            auth.login(request, user)
            messages.success(request, f'{user.username}, successful registration!')
            return HttpResponseRedirect(reverse('user:login'))
    else:
        form = UserRegistrationForm()
    return render(request, 'users/registration.html')

@login_required
def profile(request):
    if request.method == 'POST':
        form = ProfileForm(data=request.POST, isinstance=request.user,
                           files=request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile was changed')
            return HttpResponseRedirect(reverse('user:profile'))
    else:
        form = ProfileForm(isinstance=request.user)
    return render(request, 'users/profile.html', {'form': form})

def logout(request):
    auth.logout(request)
    return redirect(reverse('main:index_list'))