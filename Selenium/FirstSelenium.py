from selenium import webdriver
from selenium.webdriver.firefox.service import Service
import time
import os

# Geckodriver file path
driver_path = os.getcwd() + '/Selenium/MozillaDriver/geckodriver.exe'

service = Service(driver_path)
driver = webdriver.Firefox(service=service)

# Navigating into the URL
driver.get("https://www.facebook.com")

# Putting delay to close
time.sleep(10)
driver.quit()