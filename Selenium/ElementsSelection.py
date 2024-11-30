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
driver.get("https://www.google.com/")

# Print title
print("The title is :", driver.title)

search_box = driver.find_element(By.ID,"APjFqb")
# search_box = driver.find_element(By.NAME,"q")
search_box.send_keys("Selenuim Python")
search_box.send_keys(Keys.RETURN)

driver.implicitly_wait(5)
# Putting delay to close
time.sleep(10)
driver.quit()