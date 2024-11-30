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
driver.maximize_window()

# Navigating into the URL
driver.get("https://en.wikipedia.org/wiki/India")
# Print title
print("Navigating to", driver.title)

linkList = driver.find_elements(By.PARTIAL_LINK_TEXT,"country")
# print(links_list)

for lnk in linkList:
    print(lnk.text, " - ", lnk.get_attribute("href"))
    #print(link.get_attribute("href")) 

driver.implicitly_wait(5)

# Putting delay to close
time.sleep(10)
driver.quit()