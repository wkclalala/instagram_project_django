
from django.contrib import admin

from instagram.models import Post, instagramUser, Like, UserConnection, Comment

# Register your models here.


# Register your models here.
admin.site.register(Post)
admin.site.register(instagramUser)
admin.site.register(Like)
admin.site.register(UserConnection)
admin.site.register(Comment)