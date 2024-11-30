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
driver.get("https://demo.guru99.com/test/delete_customer.php")
# Print title
print("Navigating to", driver.title)

# Filling value
searchBox = driver.find_element(By.NAME,"cusid")
searchBox.send_keys("Sangeeth")
driver.implicitly_wait(5)
searchBox.send_keys(Keys.ENTER)
time.sleep(5)

#Handle alert
driver.implicitly_wait(5)
alert = driver.switch_to.alert
print("Alert text : ", alert.text)
alert.accept()

time.sleep(5)
driver.implicitly_wait(10)
alert = driver.switch_to.alert
print("Alert text : ", alert.text)
alert.accept()


# Putting delay to close
time.sleep(10)
driver.quit()