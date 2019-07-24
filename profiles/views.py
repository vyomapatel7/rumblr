from django.shortcuts import render
from .models import Profile, Post

def profile(request):
    profile = Profile.objects.get(user=request.user)
    post = Post.objects.filter(profile=profile)
    context = {
        'profile': profile,
        'post': post,
    }
    return render(request, 'profile.html', context)

def about(request):
	return render(request, 'about.html')

def home(request):
	profile = Profile.objects.all()
	context = {
		'profile': profile,
	}
	return render(request, 'home.html', context)
