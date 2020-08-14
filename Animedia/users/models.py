from django.db import models
from django.contrib.auth.models import User
from animelist.models import Anime,Tag

# Create your models here.
class Profile(models.Model) :
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    image = models.ImageField(default='default_profile.jpg',upload_to='profile_pics')
    aboutMe = models.TextField(blank=True)
    watchedAnime = models.ManyToManyField(Anime,blank=True,related_name='watchedAnime')
    friends = models.ManyToManyField(User,blank=True,related_name='friends')
    favouriteAnime = models.ManyToManyField(Anime,blank=True,related_name='favouriteAnime')
    favouriteDialogue = models.CharField(max_length=100)
    favouriteCharacter = models.CharField(max_length=100)

    def __str__(self) :
        return self.user.username
