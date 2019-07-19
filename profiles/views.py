from django.shortcuts import render
from .models import Profile

def profile(request, user):
	profile = Profile.objects.get(user=request.user)
    context = {
        'profile': profile
        'user': request.user
    }
    return render(request, 'profile.html', context)

def about(request):
	return render(request, 'about.html')