from bs4 import BeautifulSoup
from requests import get

user_date = input("Which Date you want to travel to ? YYYY-MM-DD: ")
response = get(url=f"https://www.billboard.com/charts/hot-100/{user_date}/")
soup = BeautifulSoup(response.content, "html.parser")

songs_list = soup.select(selector="li h3", id="title-of-a-story")
songs_list = [song.text.replace("\n", "").replace("\t", "") for song in songs_list]
print(songs_list)
