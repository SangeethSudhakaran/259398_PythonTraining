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

LinkElement = driver.find_element(By.LINK_TEXT,"most populous country")
# print(links_list)

driver.get(LinkElement.get_attribute('href'))

driver.implicitly_wait(5)
driver.back()
driver.implicitly_wait(5)
driver.forward()

# Putting delay to close
time.sleep(10)
driver.quit()