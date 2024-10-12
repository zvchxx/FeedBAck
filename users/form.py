from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
# from users.models import ProfileModel 

class RegistrationForm(UserCreationForm):
    location = forms.CharField(max_length=64, required=False) 
    link = forms.URLField(max_length=200, required=False) 

    class Meta:
        model = User
        fields = ['username', 'first_name', 'email', 'password1', 'password2']

    # def save(self, commit=True):
    #     user = super().save(commit)  
    #     profile = ProfileModel(
    #         user=user,  
    #         location=self.cleaned_data.get('location'),
    #         link=self.cleaned_data.get('link'),
         
    #     )
    #     if commit:
    #         profile.save()  
    #     return user

class LoginForm(forms.Form):
    username = forms.CharField(max_length=128)
    password = forms.CharField(max_length=128)