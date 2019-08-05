from django.forms import ModelForm
from .models import Profile, Post

class ProfileEditForm(ModelForm):
	class Meta:
		model = Profile
		fields = ('title', 'bio',)

class CreatePostForm(ModelForm):
	class Meta:
		model = Post
		fields = ('title', 'post', 'image',)