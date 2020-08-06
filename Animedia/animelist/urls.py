from django.urls import path
from . import views


urlpatterns = [
    path('', views.animeHome, name = 'animeHome'),
    path('<str:animeName>/', views.animeProfile , name = 'animeProfile'),
]  



