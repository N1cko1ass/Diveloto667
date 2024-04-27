from django.urls import path, include
from django.contrib.auth import login, logout
from django.contrib.auth.views import LoginView
from . import views
from .views import *

urlpatterns = [
    path('', views.index, name='home'),
    path('/registration', registration.as_view(), name='registration'),
    path('/authorization', authorization.as_view(), name='authorization'),
    path('/profile/main', views.profile_main, name='profile'),
    path('/profile/notifications', views.profile_notifications, name="profile_notifications"),
    path('/profile/bonuses', views.profile_bonuses, name="profile_bonuses"),
    path('logout/', logout_user, name="logout"),
]