from django.shortcuts import render
from .models import Song
import requests

def index(request):
    allSongs = Song.objects.all()
    return render(request, template_name="index.html", context={"allSongs" : allSongs})

# # views.py
# import spotipy 
# from spotipy.oauth2 import SpotifyOAuth
# from django.conf import settings
# from django.http import HttpResponseRedirect

# def spotify_auth(request):
#     # Your authentication code here
# def spotify_callback(request):
#     # Your callback handling code here
# def get_user_tracks(request):
#     # Your code for making Spotify API requests here
