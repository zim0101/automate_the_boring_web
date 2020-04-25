import time
from main.web_driver import driver


# login method, which will automate the login process
def automated_login(url: str, email: str, password: str) -> bool:
    """
    :param url: str
    :param email: str
    :param password: str
    """
    try:
        # go to the login url and wait 2 sec to load the page
        driver.get(url)
        time.sleep(2)
        # fill the login form with correct credentials
        email_field = driver.find_element_by_xpath('//*[@id="email"]')
        email_field.send_keys(email)
        password_field = driver.find_element_by_xpath('//*[@id="passwd"]')
        password_field.send_keys(password)

        # do the login action
        login_button = driver.find_element_by_xpath('//*[@id="SubmitLogin"]')
        login_button.click()

        return True
    except Exception as e:
        # anything goes wrong, close the driver
        print(e)
        driver.close()

        return False
