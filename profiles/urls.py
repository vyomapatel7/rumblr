from django.urls import path
from . import views

urlpatterns = [
    path('profiles/post/<id>/', views.post, name='post'),
    path('profiles/user/', views.myprofile, name='myprofile'),
    path('profiles/<id>/', views.profile, name='profile'),
    path('profiles/<id>/edit', views.edit_profile, name='edit_profile'),
    path('profiles/create_profile', views.create_profile, name='create'),
    path('profiles/create_post', views.create_post, name='create_post'),
]
