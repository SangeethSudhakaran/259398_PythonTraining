from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import os

# Geckodriver file path
driver_path = os.getcwd() + '/Selenium/MozillaDriver/geckodriver.exe'

service = Service(driver_path)
driver = webdriver.Firefox(service=service)

# Navigating into the URL
driver.get("https://practicetestautomation.com/practice-test-login/")

# Print title
print("Navigating to", driver.title)

inputUserId = driver.find_element(By.ID,"username")
inputPassword = driver.find_element(By.ID,"password")
buttonLogin = driver.find_element(By.ID,"submit")

print("Elements located and filing values")
inputUserId.send_keys("student")
inputPassword.send_keys("Password123")
buttonLogin.click()
driver.implicitly_wait(5)

# cehck login success
try:
    checkLoginSuccess = driver.find_element(By.TAG_NAME,"h1")
    if(checkLoginSuccess.text=="Logged In Successfully"):
        print("Logged In Successfully!")
    else:
        print("Failed to login!")
except Exception as e:
    print(e)        
    print("Failed to login")        


# Putting delay to closeex
time.sleep(10)
driver.quit()