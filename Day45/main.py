from bs4 import BeautifulSoup

with open("website.html", encoding="utf-8") as site:
    content = site.read()
soup = BeautifulSoup(content, "html.parser")

a_tags = soup.findAll("a")
h_mic = soup.find("h3", class_="heading")
selector = soup.select(".hd ")
print(h_mic)
for tag in a_tags:
    print(tag.get("href"))

print(selector)
