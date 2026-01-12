from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def login(username,password,current_url=None,wrong_username_password=None):
    driver = webdriver.Firefox()
    try:
        driver.get('https://practicetestautomation.com/practice-test-login/')
        driver.implicitly_wait(5)
        element_username=driver.find_element(By.XPATH,"//input[@name='username']")
        element_password=driver.find_element(By.XPATH,"//input[@name='password']")
        submit=driver.find_element(By.XPATH,"//button[@id='submit']")
        if current_url:
            if element_username.is_displayed():
                element_username.clear()
                element_username.send_keys(username)
                time.sleep(2)
            if element_password.is_displayed():
                element_password.clear()
                element_password.send_keys(password)
                time.sleep(2)
            submit.click()
            time.sleep(2)
            return driver.current_url
        elif wrong_username_password:
            if element_username.is_displayed():
                element_username.clear()
                element_username.send_keys(username)
                time.sleep(2)
            if element_password.is_displayed():
                element_password.clear()
                element_password.send_keys(password)
                time.sleep(2)
            submit.click()
            error_code = driver.find_element(By.XPATH, "//div[@id='error']")
            if error_code.is_displayed():
                return error_code.text
    except Exception as e:
        return False
    finally:
        driver.close()
