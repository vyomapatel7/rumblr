from django.shortcuts import render

def profile(request):
    context = {
        'profiles': profile
    }
    return render(request, 'profile.html', context)

def about(request):
	return render(request, 'about.html')