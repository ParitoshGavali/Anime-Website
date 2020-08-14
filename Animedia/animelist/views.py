from django.shortcuts import render
from django.http import HttpResponse , HttpResponseNotFound 
from django.contrib.auth.decorators import login_required

from .models import Anime,Tag

# Create your views here.


def animeHome(request) :
    return render(request , 'animelist/base.html')


def animeProfile(request , animeName) :
    data = {}
    try : 
        anime = Anime.objects.get(title=animeName)
    except :
        return HttpResponse("Anime Not Found")

    #anime name is valid , so render the data
    data['anime'] = anime
    data['genres'] = anime.genre.all()
    # requestingUser = request.user
    # data['requestingUser'] = requestingUser 
    return render(request , 'animelist/animeProfile.html' , data)
