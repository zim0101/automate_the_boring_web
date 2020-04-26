from login.login import automated_login
from order.order import visit_and_check_order_history_page
from ui.navbar_testing import check_navigation_bar
from main.urls import *
from main.constants import *
from credentials import user_email, user_password


def run_automation():
    login_result: bool = automated_login(website_login_url, user_email,
                                         user_password)
    if login_result:
        visit_and_check_order_history_page(order_history_url, order_page_title)
        check_navigation_bar()
