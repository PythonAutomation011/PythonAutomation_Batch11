from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from file_helper import check_file,remove_file

driver=webdriver.Firefox()   #browser---firefox --->
driver.get('https://the-internet.herokuapp.com/download')    #open ULR
driver.implicitly_wait(5)
file_path="C:/Users/Admin/Downloads/test_upload_file.txt"
if check_file(file_path):
    remove_file(file_path)
element=driver.find_element(By.XPATH,"//a[@href='download/test_upload_file.txt']")
element.click()
time.sleep(1)

driver.close()  # driver.quit()




















#5 manual----> firefox
# 4 browsers---->

















