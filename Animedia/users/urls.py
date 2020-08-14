from django.contrib import admin
from django.urls import path , include
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('register/', views.register  , name='register'),
    path('profile/<str:name>', views.viewProfile , name='user-profile'),
]  


