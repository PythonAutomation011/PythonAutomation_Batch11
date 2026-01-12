from selenium import webdriver

def check_auth(url,exp_title=None,exp_url=None):
    driver=webdriver.Firefox()
    driver.get(url)
    if exp_title:
        try:
            if 'The Internet' == driver.title:
                return True
            else:
                return False
        except Exception as e:
            print(e)
        finally:
            driver.quit()
    elif exp_url:
        try:
            if 'https' in driver.current_url:
                return True
            else:
                return False
        except Exception as e:
            print(e)
        finally:
            driver.quit()