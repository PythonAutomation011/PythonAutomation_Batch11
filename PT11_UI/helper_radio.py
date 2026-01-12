from selenium import webdriver
from selenium.webdriver.common.by import By
import time


def click_all_radio():
    driver=webdriver.Chrome()
    driver.get("https://stepupandlearn.in/wp-content/UI/radiobutton.html")
    l1=[]
    try:
        elements_list=driver.find_elements(By.XPATH,"//input[@type='radio']")
        for element in elements_list:
            element.click()
            l1.append(element.is_selected())
            time.sleep(1)
        return l1
    except Exception as e:
        return False
    finally:
        driver.close()


def click_radio_value(val='Java'):
    driver=webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://stepupandlearn.in/wp-content/UI/radiobutton.html")
    try:
        element=driver.find_element(By.XPATH,f"//input[@value='{val}']")
        element.click()
        time.sleep(2)
        return element.is_selected()
    except Exception as e:
        return False
    finally:
        driver.close()


