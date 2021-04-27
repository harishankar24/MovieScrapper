import requests
from bs4 import BeautifulSoup
# from os import system
# system('cls')

response = requests.get(url = "https://www.hollywoodreporter.com/lists/100-best-films-ever-hollywood-favorites-818512")
website_html = response.text
soup = BeautifulSoup(website_html, "html.parser")
all_movies = soup.find_all(name = "h1", class_ = "list-item__title")

with open("movies.txt","w") as file:
  for i in range(len(all_movies),0,-1):
    file.write(f"{100-i+1}) {all_movies[i-1].text}\n")