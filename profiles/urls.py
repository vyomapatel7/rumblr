from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('post/<id>/', views.post, name='post'),
    path('profiles/user/', views.myprofile, name='myprofile'),
    path('profiles/<id>', views.profile, name='profile'),
    path('profiles/<id>/edit', views.edit_profile, name='edit_profile'),
    path('profiles/create_profile', views.create_profile, name='create'),
    path('posts/create_post', views.create_post, name='create_post'),
    path('posts/<id>/edit', views.edit_post, name='edit_post'),
    path('posts/<id>/delete', views.delete_post, name='delete_post'),
    path('profiles/user/following', views.following, name='following'),
    path('profiles/followers/', views.follower, name='followers'),
    path('search', views.search, name='search'),
    path('profiles/<id>/follow', views.follow, name='follow'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
