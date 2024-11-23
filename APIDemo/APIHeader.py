import requests

url="https://httpbin.org/headers"
headers={"custom-Header":"Sangeeth's Value"}

response=requests.get(url,headers=headers)
print(response)
print("------------------------------------")
print(type(response))
print("------------------------------------")
print(response.headers)
print("------------------------------------")
print(response.json())