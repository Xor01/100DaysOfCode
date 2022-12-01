from bs4 import BeautifulSoup
import requests
from collections import OrderedDict

response = requests.get("https://news.ycombinator.com/")
yc_page = response.text
soup = BeautifulSoup(yc_page, "html.parser")


article_names = soup.select(".titleline")
scores = soup.select(".score")

articles_names_list = [article_name.getText() for article_name in article_names]
articles_urls_list = [article_url.select_one("a").get("href") for article_url in article_names]
articles_score_list = [int(score.getText().split()[0]) for score in scores]

highest_score = max(articles_score_list)
index = articles_score_list.index(highest_score)

article_dic = {score: [name, url] for (name, url, score) in zip(articles_names_list, articles_urls_list, articles_score_list)}

sorted_dict = OrderedDict(sorted(article_dic.items()))

print("=================Sorted=================")
for i in sorted_dict:
    print("Thumbs Up:", i)
    print("Article Name:", sorted_dict[i][0])
    print("Article URL:", sorted_dict[i][1])
    print("======================================================")
