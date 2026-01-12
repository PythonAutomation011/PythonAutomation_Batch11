from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time

class HelperDrop:
    def __init__(self):
        self.driver=webdriver.Firefox()
        self.driver.get("https://the-internet.herokuapp.com/dropdown")
        self.driver.implicitly_wait(5)
        self.element=self.driver.find_element(By.XPATH,"//select[@id='dropdown']")
    def select_by_my_value(self,val):
        self.drop=Select(self.element)
        self.drop.select_by_value(val)
        time.sleep(2)
        self.driver.close()
        return True
    def select_by_my_index(self,val):
        self.drop=Select(self.element)
        self.drop.select_by_index(val)
        time.sleep(2)
        self.driver.close()
        return True
    def select_by_my_text(self,txt):
        self.drop=Select(self.element)
        self.drop.select_by_visible_text(txt)
        time.sleep(2)
        self.driver.close()
        return True


# obj1=HelperDrop()
# obj1.select_by_my_text('Option 1')
# obj1=HelperDrop()
# obj1.select_by_my_text('Option 2')





# # drop.select_by_value('2')
# #drop.select_by_index(1)
# #drop.select_by_visible_text('Option 2')
#
# time.sleep(4)
#
#
# # for i in drop.options:
# #     print(i.text)
#
# driver.close()