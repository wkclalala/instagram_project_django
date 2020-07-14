"""django_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from instagram.views import HelloWorld, PostsView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView, addLike, UserDetailView

urlpatterns = [
    path('helloworld/', HelloWorld.as_view(), name = 'helloworld'),
    path('', PostsView.as_view(), name = 'posts'), 
    path('post/<int:pk>/', PostDetailView.as_view(), name = 'Detail Post'),
    path('post/new/', PostCreateView.as_view(), name = 'Make Post'),
    path('post/update/<int:pk>', PostUpdateView.as_view(), name = 'Update Post'),
    path('post/delete/<int:pk>', PostDeleteView.as_view(), name = 'Delete Post'),
    path('like', addLike, name='addLike'),
    path('user/<int:pk>/', UserDetailView.as_view(), name = 'Detail User'),
]
