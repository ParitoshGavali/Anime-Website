from django.shortcuts import render,redirect
from django.http import HttpResponse 
from django.contrib.auth.decorators import login_required
from .forms import UserRegistrationForm
from django.contrib.auth.models import User
from .models import Profile

# Create your views here.
    # user = models.OneToOneField(User,on_delete=models.CASCADE)
    # image = models.ImageField(default='default_profile.jpg',upload_to='profile_pics')
    # aboutMe = models.TextField(blank=True)
    # watchedAnime = models.ManyToManyField(Anime,blank=True,related_name='watchedAnime')
    # friends = models.ManyToManyField(User,blank=True,related_name='friends')
    # favouriteAnime = models.ManyToManyField(Anime,blank=True,related_name='favouriteAnime')
    # favouriteDialogue = models.CharField(max_length=100)
    # favouriteCharacter = models.CharField(max_length=100)

def register(request) :
    if request.method == "POST" :
        form = UserRegistrationForm(request.POST)
        if form.is_valid() :
            form.save()
            username = form.cleaned_data.get('username')
            user = User.objects.filter(username=username).first()
            userProfile = Profile()
            userProfile.user = user;
            userProfile.image = form.cleaned_data.get('image')
            if not userProfile.image :
                userProfile.image = 'default_profile.jpg'
            userProfile.aboutMe = form.cleaned_data.get('aboutMe')
            userProfile.favouriteDialogue = form.cleaned_data.get('favouriteDialogue')
            userProfile.favouriteCharacter = form.cleaned_data.get('favouriteCharacter')
            print(userProfile)
            userProfile.save()
            return redirect('login')
    else :
        form = UserRegistrationForm()
    return render(request , 'users/register.html' , {'form' : form})



@login_required
def viewProfile(request , name) :
    return HttpResponse("HI " + name +  " " + request.user.username)
