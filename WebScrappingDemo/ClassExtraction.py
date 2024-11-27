import requests
from bs4 import BeautifulSoup

url= "https://w3schools.com/html"
response=requests.get(url)

soup=BeautifulSoup(response.text,'html.parser')
#print(soup)

# Get the text of id tag
header = soup.find_all(id='getdiploma')
for h in header:    
    print(h.text.strip())