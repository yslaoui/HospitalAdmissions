from django import forms
from .models import *
from django.contrib.auth.models import User


class UserForm(forms.ModelForm):
    password = models.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password')

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('organization')






