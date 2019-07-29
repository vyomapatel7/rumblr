from django.urls import path
from . import views

urlpatterns = [
    path('profiles/user/', views.myprofile, name='myprofile'),
    path('profiles/<id>/', views.profile, name='profile'),
]
