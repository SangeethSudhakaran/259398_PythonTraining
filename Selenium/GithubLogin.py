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
driver.get("https://github.com/login")

# Print title
print("Navigating to", driver.title)

inputUserId = driver.find_element(By.ID,"login_field")
inputPassword = driver.find_element(By.ID,"password")

inputUserId.send_keys("sangeethcs2010@gmail.com")
inputPassword.send_keys("sangeethcs2010@gmail.com")

inputPassword.send_keys(Keys.RETURN)

driver.implicitly_wait(5)
# Putting delay to close
time.sleep(10)
driver.quit()