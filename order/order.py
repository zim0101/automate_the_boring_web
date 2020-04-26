from main.web_driver import driver


def visit_and_check_order_history_page(url: str, title: str) -> bool:
    """
    :param url: str
    :param title: str
    :return: bool
    """
    try:
        driver.get(url)
        page_title_element = driver.find_element_by_xpath(
            '//*[@id="center_column"]/h1')
        page_title = page_title_element.get_attribute('textContent')
        if page_title == title:
            return True

        return False
    except Exception as e:
        print(e)
        driver.close()

        return False
