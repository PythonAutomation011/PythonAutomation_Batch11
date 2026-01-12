from selenium import webdriver
import time

class HelpeBasic:
    def __init__(self):
        self.url="https://stepupandlearn.in/"
        self.driver=webdriver.Firefox()
    def validate_title_url(self,exp_title=None,exp_url=None):
        try:
            if exp_title:
                self.driver.get(self.url)
                return self.driver.title
            elif exp_url:
                self.driver.get(self.url)
                return self.driver.current_url
        except Exception as e:
            return None
        finally:
            self.driver.close()
# obj=HelpeBasic()
# obj.validate_title_url(exp_title=True)
# obj.validate_title_url(exp_url=True)