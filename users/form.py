from django import forms

from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth.models import User


class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'password1', 'password2']


class LoginForm(forms.Form):
    email = forms.CharField(max_length=120)
    password = forms.CharField(max_length=120)