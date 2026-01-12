from selenium import webdriver
from selenium.webdriver.common.by import By

def check_info_alert(info=None,conf=None,inp=None):
    driver = webdriver.Chrome()
    driver.get('https://the-internet.herokuapp.com/javascript_alerts')
    driver.maximize_window()
    if info:
        try:
            element = driver.find_element(By.XPATH, "//button[@onclick='jsAlert()']")
            element.click()
            var = driver.switch_to.alert
            var.accept()
            # var.send_keys('Hello')
            # var.dismiss()
            result = driver.find_element(By.ID, "result")
            return result
        except Exception as e:
            print(e)
        finally:
            driver.close()
    elif conf:
        try:
            element = driver.find_element(By.XPATH, "//button[@onclick='jsAlert()']")
            element.click()
            var = driver.switch_to.alert
            #var.accept()
            # var.send_keys('Hello')
            var.dismiss()
            result = driver.find_element(By.ID, "result")
            return result
        except Exception as e:
            print(e)
        finally:
            driver.close()
    elif inp:
        try:
            element = driver.find_element(By.XPATH, "//button[@onclick='jsPrompt()']")
            element.click()
            var = driver.switch_to.alert
            var.send_keys('Hello')
            var.accept()
            result = driver.find_element(By.ID, "result")
            return result
        except Exception as e:
            print(e)
        finally:
            driver.close()