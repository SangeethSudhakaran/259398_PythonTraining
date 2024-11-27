import requests
from bs4 import BeautifulSoup
import os
import pandas as pd

url= "https://quotes.toscrape.com/"
response=requests.get(url)

soup=BeautifulSoup(response.text,'html.parser')
#print(soup)

# quote_object = soup.find(class_="quote")
# text_object = quote_object.find(class_="text")
# print(text_object.text.strip())

# author_object = quote_object.find(class_="author")
# print(author_object.text.strip())

quotes = soup.select(".quote .text")
author = soup.select(".quote .author")
quoteData =[]
os.chdir("WebScrappingDemo")
with open("QuotesData.txt","w") as file:
    for each_quote,each_author in zip(quotes,author):
        print(each_quote.text,"-",each_author.text)
        quoteData.append({"quote" : each_quote.text,"author":each_author.text})
        file.write(each_quote.text + "-" + each_author.text+"\n")

df = pd.DataFrame(quoteData)
df.to_csv("QuoteData.csv")