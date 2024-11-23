import requests

url = "https://api.coingecko.com/api/v3/simple/price"
params = {
    "ids":"bitcoin,ethereum","vs_currencies":"inr"
}

resposnse = requests.get(url,params)
#print(resposnse.json())

final_value = resposnse.json()['ethereum']['inr']
print(final_value)