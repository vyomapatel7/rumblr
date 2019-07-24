from django.db import models
from django.conf import settings

class Post(models.Model):
	title = models.CharField(max_length=200)
	post = models.TextField(max_length=100, blank=True)
	image = models.ImageField(default='default.jpg', upload_to='picsinposts')

	def __str__(self):
		return self.title

class Profile(models.Model):
	title = models.CharField(max_length=200, blank=True, null=True)
	bio = models.TextField(max_length=500, blank=True)
	user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
	post = models.ForeignKey(Post, on_delete=models.CASCADE, blank=True, null=True)

	def __str__(self):  # this makes the username the profilesname
		return f'{self.user.username} Profile'  