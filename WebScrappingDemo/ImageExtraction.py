import requests
from bs4 import BeautifulSoup
import pandas as pd
import os

url= "https://unsplash.com/s/photos/nature"
response=requests.get(url)

soup=BeautifulSoup(response.text,'html.parser')

# Downloading single image 
images = soup.find_all('img',{"srcset":True})
image_url=images[-1]
image_url=image_url['src']
print(image_url)
i_count = 0

img_data = requests.get(image_url).content
image_path = "sample_image.jpg"

with open(image_path,"wb") as img_file_handler:
    img_file_handler.write(img_data)


#Downloading all the Images to a new folder
new_path = os.getcwd() + "\\WebScrappingDemo\\Images\\"
if not os.path.exists(new_path):
    os.makedirs(new_path)

print(f"Dowloading {len(images)} images...")
for img in images:
    i_count += 1
    image_url=img['src']

    # If the keyword is found, slice the string up to that keyword
    index = image_url.find("&crop")
    if index != -1: image_url = image_url[:index]

    # Getting image data
    img_data = requests.get(image_url).content
    
    # The name in alt is not available then creating a default name
    try:
        if(img['alt']):
            image_path = new_path +  + img['alt'] + ".jpg"           
        else:
            image_path = new_path + "downloadedImage" + i_count + ".jpg"            
    except Exception as e:
        image_path = new_path + "downloadedImage" + str(i_count) + ".jpg"
        print("Error in file name, added a default name. Exception:", e)        
    with open(image_path,"wb") as img_file_handler:
        img_file_handler.write(img_data)
        print(f"Count : {i_count}/{len(images)} Image downloaded : " + image_path)

#df = pd.DataFrame(image_data)
#print(df)
#df.to_csv("ImageData.csv")