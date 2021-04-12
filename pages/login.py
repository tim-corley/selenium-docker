"""
This module contains LoginPage,
the page object for the Hacker News login / signup page
"""
import os
from dotenv import load_dotenv
from utils.wrapper import PageObject, HTMLElement
from utils.logger import Logger, info

logger = Logger().get_logger()


class LoginPage(PageObject):
    load_dotenv()
    username_input = HTMLElement(css='input[name="acct"]')
    password_input = HTMLElement(css='input[name="pw"]')
    login_button = HTMLElement(css='input[value="login"]')
    USERNAME = os.getenv('USERNAME')
    PASSWORD = os.getenv('PASSWORD')

    def __init__(self, webdriver):
        # super().__init__(browser)
        self.webdriver = webdriver

    def input_login_credentials(self):
        self.username_input.send_keys(self.USERNAME)
        self.password_input.send_keys(self.PASSWORD)
        info(logger, 'successfully input username & password')

    def click_login_button(self):
        self.login_button.click()
        info(logger, 'clicked login button')

    def user_login(self):
        self.input_login_credentials()
        self.click_login_button()