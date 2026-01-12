from selenium import webdriver
import time

driver=webdriver.Firefox()

driver.get('https://admin:admin@the-internet.herokuapp.com/basic_auth')
print(driver.title)
print(driver.current_url)
time.sleep(5)

driver.quit()












import sys
sys.exit(0)
from selenium import webdriver
import time

driver=webdriver.Firefox()
driver.get('https://the-internet.herokuapp.com/')
driver.switch_to.new_window('window')
#driver.switch_to.new_window('tab')
time.sleep(3)
driver.get('https://the-internet.herokuapp.com/')
time.sleep(3)
driver.quite()  # close the single window/tab   quite()


'''
quite----> all open windows


close----> single window



'''







































import sys
sys.exit(0)
from selenium import webdriver
import time
driver=webdriver.Firefox()
driver.get('https://stepupandlearn.in/')
print('title:',driver.title)
time.sleep(5)
driver.get('https://www.amazon.in/')
print('title:',driver.title)
time.sleep(5)
driver.back()
print('after back title:',driver.title)
time.sleep(5)
driver.forward()
print('after forward title:',driver.title)

driver.close()

























import sys
sys.exit(0)
from selenium import webdriver
import time

driver=webdriver.Firefox()
driver.get('https://stepupandlearn.in/')

print('title is:',driver.title)
print('url is',driver.current_url)
print('source code is :',driver.page_source)

driver.close()













import sys
sys.exit(0)
def open_browser(browsername):
    try:
        if browsername=='C':
            driver=webdriver.Chrome()
            driver.get('https://stepupandlearn.in/')
            time.sleep(5)
            driver.close()
        elif browsername=='F':
            driver = webdriver.Firefox()
            driver.get('https://stepupandlearn.in/')
            time.sleep(5)
            driver.close()
    except Exception as e:
        print(e)

open_browser('C')
open_browser('F')
open_browser('I')



















import sys
sys.exit(0)
from selenium import webdriver
import time
driver=webdriver.Firefox()
driver.get('https://stepupandlearn.in/')   #open url
driver.maximize_window()
time.sleep(5)
for i in range(5):
    driver.save_screenshot(f'sample{i}.png')
driver.minimize_window()
driver.maximize_window()
time.sleep(5)
driver.close()  #close the browser open by script