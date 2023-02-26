from bs4 import BeautifulSoup
import requests
import re

url = "https://www.nytimes.com/"
req = requests.get(url)
soup = BeautifulSoup(req.text, "html.parser")
headlines = soup.find_all(class_="css-xdandi")

with open("NYT.txt", "w") as open_file:
    for headline in headlines:
        open_file.write(headline.text.strip())
