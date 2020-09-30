# Anime-Website (Animedia)
To create a Social Media platform for anime nerds, where they can rate and keeptrack of the anime, interact in discussion forums and post their thoughts as posts.

## How to run : 
To add the necessary libraries run the following after the clonning is done.
Please install pip module for downloading python packages.
```
pip install django-crispy-forms
pip install Pillow
```
To run the website first you need to configure the database with the following :
```
python3 manage.py migrate --run-syncdb
python3 manage.py migrate makemigrations
python3 manage.py migrate
```
Now to run the server : `python3 manage.py runserver`
Some additional commands 
- `python3 manage.py createsuperuser` | To create an admin in Django

> <b>NOTE</b> : Never add migrations files while commiting your changes

## Targets to be achieved : 
1. <b>Base mode</b> : Basic Structure
- :heavy_check_mark: Making an anime database 
- Backend for user (User model + basic pages like login, homepage, logout)
- Bcakend for animelist (Animelist model + animepage, rating and comments)
- Wakeau (posts created by user)
- Search bar for searching users and animes

2. <b>SSJ</b> : Basic Features
- Additional features of the user like his favourates
- Animedatabase handelling app in Django 
- Adding disscussion forums for anime where people can discuss about the latest episode

3. <b>SSJ 2</b> : Visual Overhaul 
- Finalising theme and visuals
- Finalising name and logo
- Fixing some unknown bugs

4. <b>SSJ 3</b> : Additional Features 
5. <b>SSG</b> : Hosting
6. <b>SSB</b> : Expansion phase
7. <b>UI</b> : Making an android app
