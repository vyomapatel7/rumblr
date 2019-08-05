from django.shortcuts import render, redirect, reverse
from .models import Profile, Post
from profiles.forms import ProfileEditForm, CreatePostForm

def create_post(request):
    form_class = CreatePostForm
    if request.method == 'POST':
        form = form_class(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect('myprofile')

    else:
        form = form_class()

    return render(request, 'profiles/create_post.html', {
        'form': form,
    })


def profile(request, id):
    profile = Profile.objects.get(id=id)
    post = Post.objects.filter(profile=profile)
    context = {
        'profile': profile,
        'post': post,
    }
    return render(request, 'profile.html', context)


def post(request, id):
    post = Post.objects.get(id=id)
    profile = Profile.objects.get(post=post)
    context = {
        'post': post,
        'profile': profile,
    }
    return render(request, 'post.html', context)


def edit_profile(request, id):
    profile = Profile.objects.get(id=id)
    form_class = ProfileEditForm
    if request.method == "POST":
        form = form_class(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile', id=profile.id)
    
    else:
        form = form_class(instance=profile)

    return render(request, 'edit_profile.html', {
        'profile': profile,
        'form': form,
    })


def create_profile(request):
    profile = None
    if Profile.objects.filter(user=request.user).exists():
        profile = Profile.objects.get(user=request.user)
    form_class = ProfileEditForm
    if request.method == 'POST':
        form = form_class(request.POST, instance=profile)
        if Profile.objects.filter(user=request.user).exists():
            profile = Profile.objects.get(user=request.user)
            return redirect(reverse('edit_profile', kwargs={'id': profile.id}))
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
            return redirect('home')
        form = form_class(request.POST)
        if Profile.objects.get(user=request.user):
            if form.is_valid():
                profile = form.save(commit=False)
                profile.user = request.user
                profile.save()
                return redirect('profile')
    else:
        form_class = ProfileEditForm
        form = form_class(instance=profile)

    return render(request, 'create_profile.html', {
        'form': form,
        'profile': profile,
        }) 


def myprofile(request):
    profile = Profile.objects.get(user=request.user)
    form_class = ProfileEditForm
    if Profile.objects.filter(user=request.user).exists():
        profile = Profile.objects.get(user=request.user)
        post = Post.objects.filter(profile=profile)
        context = {
        'profile': profile,
        'post': post,
        }
        return render(request, 'profile.html', context)
    else:
        form = form_class(instance=profile)

def about(request):
	return render(request, 'about.html')

def home(request):
	profile = Profile.objects.all()
	context = {
		'profile': profile,
	}
	return render(request, 'home.html', context)


