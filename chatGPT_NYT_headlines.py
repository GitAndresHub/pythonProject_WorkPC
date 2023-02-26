import requests
from bs4 import BeautifulSoup

url = "https://www.nytimes.com/"
r = requests.get(url)
soup = BeautifulSoup(r.content, "html.parser")

# Find all the article titles on the page
titles = soup.find_all(class_="css-xdandi")
for title in titles:
    print(title.text.strip())
