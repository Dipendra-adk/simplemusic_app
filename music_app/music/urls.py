
from django.urls import path
from .import views
urlpatterns = [
    # path('vo',views.ok),
    path('',views.index, name="index"),
    
]

# # urls.py
# from django.urls import path
# from . import views

# urlpatterns = [
#     path('spotify-auth/', views.spotify_auth, name='spotify-auth'),
# ]
