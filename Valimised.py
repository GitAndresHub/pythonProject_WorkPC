from bs4 import BeautifulSoup
import requests

url = "https://www.valimised.ee"
req = requests.get(url)
soup = BeautifulSoup(req.text, "html.parser")
headlines = soup.find_all(class_="percent mb-3 mb-xl-0")
for headline in headlines:
    print(headline.text.strip())

