from bs4 import BeautifulSoup
import requests
import re

url = "https://www.nytimes.com/"
req = requests.get(url)
soup = BeautifulSoup(req.text, "html.parser")
headlines = soup.find_all(class_="css-xdandi")
for headline in headlines:
    print(headline.text.strip())