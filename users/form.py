from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from users.models import ProfileUserModel 

class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'email', 'password1', 'password2']
        

class LoginForm(forms.Form):
    username = forms.CharField(max_length=128)
    password = forms.CharField(max_length=128)