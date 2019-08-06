from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
	@property
	def has_profile(self):
		if self.profile:
			return True

	def __str__(self):
		return self.email

	def doesnothave_profile(self):
		if not self.profile:
			return True
