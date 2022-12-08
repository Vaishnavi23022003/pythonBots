from bs4 import BeautifulSoup
import requests

res=requests.get("https://www.empireonline.com/movies/features/best-movies-2/")

soup=BeautifulSoup(res.text,"html.parser")

_movies=soup.select(".listicle-item-content p a")

movies=[]

for i in range(0,len(_movies)):
     if "Read Empire"==_movies[i].text[:11]:
          movies.append(_movies[i].text[24:])

movies.reverse()
print(movies)

with open("movies.txt","w") as file:
     for i in range(0,len(movies)):
          file.write(f"{i+1}) {movies[i]}\n")