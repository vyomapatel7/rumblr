from django.db import models
from django.conf import settings

class Profile(models.Model):
	bio = models.TextField(max_length=500, blank=True)
	user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

	def __str__(self):
		return f'{self.user.username} Profile'