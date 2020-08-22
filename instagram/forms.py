from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm

from instagram.models import instagramUser, Post

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = instagramUser
        fields = ('username','email','profile_pic')

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['author']
        widgets = {'name': forms.HiddenInput()}