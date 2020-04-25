import time
from main.web_driver import driver


def visit_order_history(url):
    try:
        driver.get(url)
        time.sleep(2)

    except Exception as e:
        print(e)
        driver.close()
