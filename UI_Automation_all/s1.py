
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.keys import Keys

driver=webdriver.Firefox()
driver.get("https://stepupandlearn.in/")

element=driver.find_element(By.TAG_NAME,"body")

for i in range(10):
    element.send_keys(Keys.DOWN)
    time.sleep(1)

for i in range(10):
    element.send_keys(Keys.UP)
    time.sleep(1)



driver.close()