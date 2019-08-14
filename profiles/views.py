from django.shortcuts import render, redirect, reverse, get_object_or_404
from .models import Profile, Post, Connection
from users.models import CustomUser
from profiles.forms import ProfileEditForm, CreatePostForm


def search(request):
    if request.method == 'GET':
        query = request.GET.get('q')
        submitbutton = request.GET.get('submit')
        if query is not None:
            lookups = Q(title__icontains=query) | Q(content__icontains=query)
            results = Post.objects.filter(lookups).distinct()
            context ={'results': results,
                     'submitbutton': submitbutton}
            return render(request, 'search.html', context)

        else:
            return render(request, 'search.html')

    else:
        return render(request, 'search.html')


def follower(request):
    follower = Connection.objects.filter(following=request.user)
    context = {
        'following': following,
        'follower': follower,
    }
    return render(request, 'followers.html', context)


def following(request):
    following = Connection.objects.filter(follower=request.user)
    context = {
        'following': following,
    }
    return render(request, 'following.html', context)


def delete_post(request, id):
    post = Post.objects.get(id=id)
    post.delete()
    return redirect('myprofile')

def edit_post(request, id):
    post = Post.objects.get(id=id)
    form_class = CreatePostForm
    if request.method == 'POST':
        form = form_class(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('myprofile')
    else:
        form = form_class(instance=post)

    return render(request, 'edit_post.html', {
        'post': post,
        'form': form,
    })


def create_post(request):
    form_class = CreatePostForm
    if request.method == 'POST':
        form = form_class(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            my_p = Profile.objects.get(user=request.user)
            post.profile = my_p
            post.save()
            return redirect('myprofile', id=profile.id)

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


