import requests
from bs4 import BeautifulSoup
import pandas as pd
import os

url= "https://www.bbc.com/news"
response=requests.get(url)

soup=BeautifulSoup(response.text,'html.parser')

# Get the text of links using class
cardData = []
cards = soup.find_all(class_='sc-8ea7699c-3')

for card in cards:
    cardData.append(card.text.strip())

# Create DF, Export cards as csv
df = pd.DataFrame(cardData)
print(df)

os.chdir("WebScrappingDemo")
df.to_csv("BBCNewsData.csv")
print("CSV export completed")