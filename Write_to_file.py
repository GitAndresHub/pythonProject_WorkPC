from bs4 import BeautifulSoup
import requests

url = "https://www.nytimes.com/"
req = requests.get(url)
soup = BeautifulSoup(req.text, "html.parser")
headlines = soup.find_all(class_="css-xdandi")

file_name = input("Please enter file name: ")

with open(f"C:/Users/Arvuti3/Documents/{file_name}.txt", "w") as open_file:
    for headline in headlines:
        open_file.write(headline.text.strip() + "\n")
