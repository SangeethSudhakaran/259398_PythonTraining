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
driver.get("https://www.wikipedia.org/")

# Print title
print("Navigating to", driver.title)

inputSerach = driver.find_element(By.XPATH,"""//*[@id="searchInput"]""")
buttonEnter = driver.find_element(By.XPATH,"""//*[@id="search-form"]/fieldset/button/i""")

inputSerach.send_keys("India")
buttonEnter.click()
driver.implicitly_wait(5)

headerElement = driver.find_element(By.XPATH,"""//h2[contains(text(),'Etymology')]""")
print("Elemet found and the text is :", headerElement.text)
print("Elemet found and the id is :", headerElement.id)
# Putting delay to close
time.sleep(10)
driver.quit()