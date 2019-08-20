from django.db import models
from django.conf import settings


class Profile(models.Model):
    title = models.CharField(max_length=200, blank=True, null=True)
    bio = models.TextField(max_length=500, blank=True)
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True
    )
    profile_pic = models.ImageField(
        default="default.jpg", upload_to="profile_pics"
    )

    def __str__(self):
        return f"{self.user.username} Profile"


class Post(models.Model):
    title = models.CharField(max_length=200)
    post = models.TextField(max_length=100, blank=True)
    image = models.ImageField(default="default.jpg", upload_to="picsinposts")
    profile = models.ForeignKey(
        Profile, on_delete=models.CASCADE, blank=True, null=True
    )

    def __str__(self):
        return self.title


class Connection(models.Model):
    follower = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="friendship_creator_set",
    )
    following = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="follow_set"
    )

    def __str__(self):
        return self.follower.profile.title
