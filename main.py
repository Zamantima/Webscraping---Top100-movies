import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

movie_file = "movies.txt"
response = requests.get(URL)
yc_web_page = response.text
soup = BeautifulSoup(yc_web_page, "html.parser")

titles = soup.find_all(name="h3", class_="title")

with open(movie_file, 'w', encoding="utf8") as data:
    for movie in titles[::-1]:
        m = movie.getText()
        data.write(f"{m}\n")

