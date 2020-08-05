from django.db import models

# Create your models here.
class Tag(models.Model) :
    name = models.CharField(max_length=100)

    def __str__(self) :
        return self.name



class Anime(models.Model) :
    title = models.CharField(max_length=200)
    genre = models.ManyToManyField('Tag',blank=True)
    image = models.ImageField(default='default.jpeg',upload_to='anime_pics')
    totalEpisodes = models.IntegerField(default=0)
    releaseYear = models.IntegerField(default=0) 
    ongoingStatus = models.BooleanField(default=0)
    rating = models.IntegerField(default=0)
    studios = models.CharField(max_length=100,default='Other')
    producers = models.CharField(max_length=100,default='Other')  
    source = models.CharField(max_length=100,default='Other') 

    def __str__(self):
        return self.title







