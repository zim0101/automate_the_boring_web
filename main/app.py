from login.login import automated_login
from order.order import visit_order_history
from main.urls import *
from credentials import user_email, user_password


def run_automation():
    login_result: bool = automated_login(website_login_url, user_email,
                                         user_password)
    if login_result:
        visit_order_history(order_history_url)
