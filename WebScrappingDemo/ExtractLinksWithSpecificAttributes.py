import requests
from bs4 import BeautifulSoup

url= "https://www.python.org/"
response=requests.get(url)

soup=BeautifulSoup(response.text,'html.parser')
#print(soup)

# Get the text of links and filter
links = soup.find_all('a',href=True)
for link in links:
    if link['href'].startswith("https://wiki"):
        print(link['href'])