import requests
from bs4 import BeautifulSoup

url = "https://www.nytimes.com/"
r = requests.get(url)
soup = BeautifulSoup(r.content, "html.parser")

# Find all the article titles on the page
titles = soup.find_all(class_="css-1vhd4r esl82me2")
for title in titles:
    print(title.text.strip())
