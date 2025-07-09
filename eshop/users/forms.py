from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from .models import User


class UserLoginForm(AuthenticationForm):
    username = forms.CharField()
    password = forms.CharField()


    class Meta:
        model = User
        fields = ['username', 'password']

class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('name',
                  'surname',
                  'username',
                  'email',
                  'password1',
                  'password2',)
        name = forms.CharField()
        surname = forms.CharField()
        username = forms.CharField()
        email = forms.CharField()
        password1 = forms.CharField()
        password2 = forms.CharField()


class ProfileForm(UserChangeForm):
    class Meta:
        model = User
        fields = ('image',
                  'name',
                  'surname',
                  'username',
                  'email',)
        image = forms.ImageField(required=False)
        name = forms.CharField()
        surname = forms.CharField()
        username = forms.CharField()
        email = forms.CharField()
        