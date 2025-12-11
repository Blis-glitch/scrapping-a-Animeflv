import requests
from bs4 import BeautifulSoup


website = 'https://www3.animeflv.net/anime/bleach-tv'
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"}


result = requests.get(website, headers = headers )

soup = BeautifulSoup(result.text, 'lxml')
#print(soup. prettify())

title = soup.find('h1', class_= 'Title').get_text()

transcript = soup.find('div', class_= 'Description').get_text()

print(title)
print(transcript)
