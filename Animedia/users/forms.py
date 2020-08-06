from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserRegistrationForm(UserCreationForm) :
    image = forms.ImageField(required=False , label="Image")
    aboutMe = forms.CharField(widget=forms.Textarea(attrs={"rows":5,"cols":20}),label="About Me")
    # watchedAnime = forms.MultipleChoiceField(choices=animes,widget=forms.SelectMultiple() , label="Select Animes You Watched fully")
    # watchedAnime = forms.ManyToManyField(Anime,blank=True,related_name='watchedAnime)
    # favouriteAnime = forms.MultipleChoiceField(choices=animes,widget=forms.SelectMultiple() , label="Select Your favourite Anime")
    favouriteDialogue = forms.CharField(max_length=100 , label="Your Favourite Dialogue")
    favouriteCharacter = forms.CharField(max_length=100 , label="Your Favourite Character")

    class meta : 
        model = User 
        fields = [ 
                    'image', 
                    'aboutMe', 
                    'favouriteDialogue',
                    'favouriteCharacter',
                ]

    
