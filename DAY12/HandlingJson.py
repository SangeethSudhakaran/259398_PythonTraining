import requests
import pandas pd

url = "https://api.coingecko.com/api/v3/simple/price"
params = {
    "ids":"bitcoin,ethereum","vs_currencies":"inr"
}

resposnse = requests.get(url,params)
#print(resposnse.json())

#print(type(resposnse.json()))