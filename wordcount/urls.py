from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('login',views.login, name="login" ),
    path('', views.home, name="home" ),
    path('count', views.count),
    path('about', views.about, name="about"),
]
