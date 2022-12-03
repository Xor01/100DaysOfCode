from bs4 import BeautifulSoup
from requests import get
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials, SpotifyOAuth
from os import environ

url = "https://api.spotify.com/"

params = {
    "ids": ["https://open.spotify.com/track/3WY0iazRPHOlIq6CdbKLZ6?si=762a499a1b494d0b"]
}

res = get(url=url, params=params)
print(res)
