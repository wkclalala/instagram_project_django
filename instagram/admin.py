
from django.contrib import admin

from instagram.models import Post, instagramUser, Like, UserConnection

# Register your models here.


# Register your models here.
admin.site.register(Post)
admin.site.register(instagramUser)
admin.site.register(Like)
admin.site.register(UserConnection)