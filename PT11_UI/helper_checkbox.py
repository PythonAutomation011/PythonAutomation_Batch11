from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def click_checkbox(all=None,position=None):
    driver = webdriver.Firefox()
    driver.get('https://stepupandlearn.in/wp-content/UI/checkboxes.html')
    elements = driver.find_elements(By.XPATH, "//input[@type='checkbox']")
    try:
        if all:
            for i in elements:
                if not i.is_selected():
                    i.click()
                    time.sleep(1)
                    driver.save_screenshot(f'pic_{i}.png')
                    return True
        elif position:
            elements[position].click()
            return True
    except Exception as e:
        print(e)
    finally:
        driver.quit()
# print(elements[1].is_selected())

# for ele in elements:
#     ele.click()
#     time.sleep(2)
