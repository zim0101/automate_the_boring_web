from main.web_driver import driver
from main.constants import main_nav_elements


def check_navigation_bar() -> bool:
    """
    :return: bool
    """
    nav_bar_ul = driver.find_element_by_xpath('//*[@id="block_top_menu"]/ul')
    nav_li_elements = nav_bar_ul.find_elements_by_tag_name('li')
    nav_elements = main_nav_elements
    nav_elements_to_check = []
    for li in nav_li_elements:
        nav_elements_to_check.append(li.text)

    nav_elements_to_check = filter(None, nav_elements_to_check)
    nav_has_all_menu = all(
        element in nav_elements for element in nav_elements_to_check)

    if nav_has_all_menu:
        return True

    return False
