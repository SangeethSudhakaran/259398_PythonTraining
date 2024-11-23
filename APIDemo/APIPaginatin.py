import requests
import pandas as pd

page_range = 5
page_limit = 5
master_list = [] 
for page_number in range(page_range):
    url="https://jsonplaceholder.typicode.com/posts"
    params = {"_page" : page_number, "_limit":page_limit}
    response = requests.get(url,params=params)
    print(pd.DataFrame(response.json()))
    print("-----------------------------------------------------------------------------------------------------------")
    print("         *** Page:",page_number+1,"of",page_range, "***\n\n ")