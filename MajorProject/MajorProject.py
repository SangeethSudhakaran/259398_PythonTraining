from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import os
import pandas as pd

# Geckodriver file path
driver_path = os.getcwd() + '/Selenium/MozillaDriver/geckodriver.exe'
serachHistoryFilePath = os.getcwd() + '/MajorProject/MoviesSearchHistory.csv'

service = Service(driver_path)
driver = webdriver.Firefox(service=service)
movieDetails=[]

# Menu
def Menu():
  while True:
    print("\n\nHello! user Welcome to Movie Searching!")
    print("------------------------------------------------")
    print("Choose your options from below :-")
    print("1. Search for a Movie by name")
    print("2. Save the serch history to disk")
    print("3. Exit")
    print("------------------------------------------------\n\n")
    
    # take input from user
    userInput = input("Enter your choice : ")                                             

    if(userInput=="1"):
      SearchMovie()
    elif(userInput=="2"):
      ExportHistory()
    elif(userInput=="3"):                              
      ExitApp()
    else:
      print("Invalid choice!")

def SearchMovie():
  try:
    print("Enter the movie name to serch on IMDB")  
    movieKeyword = input()

    # Navigating into the URL
    driver.get("https://www.imdb.com")
    # Print title
    print("Navigating to", driver.title)

    Searchbar = driver.find_element(By.ID,"suggestion-search")
    SearchButton = driver.find_element(By.ID,"suggestion-search-button")
    movieDetails=""

    print("Elements located and filing values")
    Searchbar.send_keys(movieKeyword)
    SearchButton.click()    
    driver.implicitly_wait(5)

    firstItemInMovieList = driver.find_element(By.XPATH,"//div[@class='ipc-metadata-list-summary-item__tc']/a")
    firstItemInMovieList.click()

    GetMovieDetails(d=driver)

  except Exception as e:   
    print("Exception in movie search:",e) 


def GetMovieDetails(d):
    d.implicitly_wait(5)
    startDetails=""
    stars = d.find_elements(By.XPATH,"//li[@data-testid='title-pc-principal-credit']//a[normalize-space(text())='Stars']/following-sibling::div/ul/li")
    for eachstar in stars:
      if len(eachstar.text) > 0 : startDetails += (eachstar.text," - " + eachstar.text)[len(startDetails)>0]
  
    movieDetails.append({'Title' : d.find_element(By.XPATH,"//h1[@data-testid='hero__pageTitle']//span").text,
                         'Stars' : startDetails,
                         'Rating' : d.find_element(By.XPATH,"//div[@data-testid='hero-rating-bar__aggregate-rating__score']//span").text + "/10",
                         'Director' : d.find_element(By.XPATH,"//li[@data-testid='title-pc-principal-credit']//a").text,
                         'Plot' : d.find_element(By.XPATH,"//p[@data-testid='plot']//span[@data-testid='plot-xl']").text})

def ExportHistory():
  df = pd.DataFrame(movieDetails)
  print(df)
  df.to_csv(serachHistoryFilePath,index=False)

def ExitApp():
  print("Thankyou user!") 
  driver.quit()

Menu()     