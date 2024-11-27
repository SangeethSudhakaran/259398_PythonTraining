import requests
from bs4 import BeautifulSoup
import os
import pandas as pd

url= "https://en.wikipedia.org/wiki/List_of_countries_by_population_(United_Nations)"
response=requests.get(url)

soup=BeautifulSoup(response.text,'html.parser')

#Get table
table = soup.find('table')

#Read table header
headers = []
for th in table.find_all('th'):
    headers.append(th.text.strip())

#Read table data
rows = []
for row in table.find_all('tr'):
    cells = row.find_all('td')
    if cells:
        row_data = [cell.text.strip() for cell in cells]
        rows.append(row_data)

#Print DF
df = pd.DataFrame(rows, columns=headers)
print(df)

#Export to CSV
os.chdir("WebScrappingDemo")

df.to_csv("CountryPopulation.csv",index=False)
print("CSV export completed")