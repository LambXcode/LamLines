from django.urls import path
from django.contrib import admin
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('users/login', views.index2, name='root'),
    path("user",views.index2,name="user"),
    path('register',views.register, name='register'),
    path("login",views.login_view,name="login"),
    path("logout",views.logout_view,name="logout")
]

