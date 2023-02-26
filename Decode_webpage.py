from bs4 import BeautifulSoup
import requests
url = "https://www.nytimes.com/"
req = requests.get(url)
soup = BeautifulSoup(req.text, "html.parser")
print(soup.find_all("h3"))
