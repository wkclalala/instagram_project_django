from django.db import models
from django.urls import reverse
from django.contrib.auth.models import AbstractUser
from imagekit.models import ProcessedImageField

# Create your models here.

class instagramUser(AbstractUser):
    profile_pic = ProcessedImageField(
        upload_to='static/images/profiles',
        format='JPEG',
        options={'quality':100},
        blank=True,
        null=True
    )

    def get_followees(self):
        followees = UserConnection.objects.filter(follower=self)
        return followees
    
    def get_followers(self):
        followers = UserConnection.objects.filter(followee = self)
        return followers

    def is_followed_by(self, user):
        followers = UserConnection.objects.filter(followee = self)
        return followers.filter(follower=user).exists()


class Post(models.Model):
    author = models.ForeignKey(
        instagramUser,
        on_delete = models.CASCADE,
        related_name = 'my_posts'
    )
    title = models.TextField(blank=True, null=True)
    image = ProcessedImageField(
        upload_to='static/images/posts',
        format='JPEG',
        options={'quality':100},
        blank=True,
        null=True
    )

    def get_absolute_url(self):
        return reverse("Detail Post", args = [str(self.id)])

    def get_like_count(self):
        return self.likes.count()



class Like(models.Model):
    post = models.ForeignKey(
        Post,
        on_delete = models.CASCADE,
        related_name = 'likes')
    user = models.ForeignKey(
        instagramUser,
        on_delete = models.CASCADE,
        related_name = 'likes'
    )

    class Meta:
        unique_together = ("post", "user")

    def __str__(self):
        return 'Like: ' + self.user.username + ' likes ' + self.post.title

class UserConnection(models.Model):
    created = models.DateTimeField(auto_now_add=True,editable=False)
    follower = models.ForeignKey(
        instagramUser,
        on_delete = models.CASCADE,
        related_name = "follower_set"
    )
    followee = models.ForeignKey(
        instagramUser,
        on_delete = models.CASCADE,
        related_name = "followee_set"
    )

    def __str__(self):
        return self.follower.username + ' follows ' + self.followee.username