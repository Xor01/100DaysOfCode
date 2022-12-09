import spotipy
from os import environ
from bs4 import BeautifulSoup
from requests import get


redirect_url = "http://localhost:1234/callback/"
client_id = environ["client_id"]
client_secret = environ["client_secret"]
scope = "user-read-currently-playing playlist-modify-private playlist-modify-public"
oAuth_obj = spotipy.SpotifyOAuth(client_id=client_id,
                                 client_secret=client_secret,
                                 redirect_uri=redirect_url,
                                 scope=scope,
                                 )

try:
    token = oAuth_obj.get_cached_token()["access_token"]
except:
    token = oAuth_obj.get_access_token()["access_token"]
spotify_obj = spotipy.Spotify(auth=token)

def add_track(track_name, playlist_id):
    try:
        search_res = spotify_obj.search(track_name, limit=1, type="track")
        if search_res["tracks"]["items"][0]:
            track = search_res["tracks"]["items"][0]["uri"]
            spotify_obj.playlist_add_items(playlist_id, [track])
            print("Track has been added successfully")
    except KeyError:
        print("Error")
    except IndexError:
        print("No Track Found")

def get_songs_name(user_date):
    response = get(url=f"https://www.billboard.com/charts/hot-100/{user_date}/")
    soup = BeautifulSoup(response.content, "html.parser")

    songs_list = soup.select(selector="li h3", id="title-of-a-story")
    songs_list = [song.text.replace("\n", "").replace("\t", "") for song in songs_list]
    return songs_list

def creat_playlist(playlist_name, public=False):
    user_name = spotify_obj.current_user()["uri"].split(":")[2]
    try:
        playlist_creat = spotify_obj.user_playlist_create(user_name, playlist_name, public=public)
        print("Playlist Successfully Created")
        return playlist_creat['uri']
    except PermissionError:
        print("Something Wrong Happened")
        return None

def main():
    user_date = input("Which Date you want to travel to ? YYYY-MM-DD: ")
    songs_list = get_songs_name(user_date)
    playlist_id = creat_playlist("Billboard Hot 100 In " + user_date)
    if songs_list and playlist_id:
        for song in songs_list:
            add_track(song, playlist_id)
    else:
        print("Error: Something Wrong Happened")

if __name__ == '__main__':
    main()
