from selenium import webdriver
from selenium.webdriver.common.by import By
import time


driver = webdriver.Firefox()


LOCATOR = "//*[contains(text(), '%s')]"

text = 'About'

driver.get("https://investorrelations.bankofireland.com/")
el = driver.find_element(By.XPATH, LOCATOR.replace('%s', text))
item= (el.get_attribute('innerHTML'))
time.sleep(2)
print(item)
driver.quit()

