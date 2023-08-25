from bs4 import BeautifulSoup
import requests

URL = "https://www.empireonline.com/movies/features/best-movies-century/"

response = requests.get(URL)
web_page = response.text

soup = BeautifulSoup(web_page, "html.parser")
movies_headings = soup.find_all("h3", class_="listicleItem_listicle-item__title__hW_Kn")
with open("movies.txt", 'a') as f:
    for movie_heading in movies_headings[::-1]:
        f.write(f"{movie_heading.getText()}\n")
