import  requests
import time

url ="https://api.open-meteo.com/v1/forecast"
params = {
    "latitude":12.9719,
    "longitude":77.5937,
    "current_weather":"true"
}

response=requests.get(url,params)
print(response.json()['current_weather'])

if(response.status_code==200):
    print("Everything good")
elif(response.status_code==429):
    print("Rate limit exceeded")
    time.sleep(60)
else:
    print("Some other issue failing this request")        
