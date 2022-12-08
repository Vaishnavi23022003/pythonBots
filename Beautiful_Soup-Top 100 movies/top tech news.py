from bs4 import BeautifulSoup
import requests

res=requests.get("https://news.ycombinator.com/")

soup=BeautifulSoup(res.text,"html.parser")
article_tag=soup.find_all("a",class_="storylink")

article_titles=[title.text for title in article_tag]
article_links=[link.get("href") for link in article_tag]
article_score=[int(score.text.split()[0]) for score in soup.select(".subtext .score")]

max_index=article_score.index(max(article_score))

print("The max score is :",article_score[max_index])
print("Title :",article_titles[max_index])
print("Link :",article_links[max_index])
