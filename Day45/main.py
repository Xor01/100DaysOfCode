from bs4 import BeautifulSoup
from requests import get

response = get(url="https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best"
                   "-movies-2/").text
soup = BeautifulSoup(response, "html.parser")
movies = soup.select("h3")

movies_list = [movie.text for movie in movies]
movies_list.reverse()

with open("movies.txt", 'w', encoding="utf-8") as file:
    for movie in movies_list:
        file.write(movie + "\n")
