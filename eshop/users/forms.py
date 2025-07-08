from django import forms
from django.contrib.auth.forms import AuthenticationForm
from .models import User


class UseerLoginForm(AuthenticationForm):
    username = forms.CharField()
    password = forms.CharField()


    class Meta:
        model = User
        fields = ['username', 'password']
