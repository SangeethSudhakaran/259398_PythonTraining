import requests
import pandas as pd
url="https://wizard-world-api.herokuapp.com/Spells"

response= requests.get(url)
print(response)
df=pd.DataFrame(response.json())
print(df[["name","incantation","type","light"]])