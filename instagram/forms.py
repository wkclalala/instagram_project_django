from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm

from instagram.models import instagramUser

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = instagramUser
        fields = ('username','email','profile_pic')