from selenium import webdriver
from selenium.webdriver.common.by import By
import time


driver = webdriver.Firefox()

driver.get("https://www.google.ie/")
url = driver.current_url
print(url)
assert url == "https://www.google.ie/","Error!! not equal"
driver.quit()

