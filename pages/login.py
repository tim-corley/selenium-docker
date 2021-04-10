"""
This module contains LoginPage,
the page object for the Hacker News login / signup page
"""
import os
from dotenv import load_dotenv
from pages.basepage import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class LoginPage(BasePage):
    load_dotenv()
    USERNAME_INPUT = (By.CSS_SELECTOR, 'input[name="acct"]')
    PASSWORD_INPUT = (By.CSS_SELECTOR, 'input[name="pw"]')
    LOGIN_BUTTON = (By.CSS_SELECTOR, 'input[value="login"]')
    USERNAME = os.getenv('USERNAME')
    PASSWORD = os.getenv('PASSWORD')

    def __init__(self, browser):
        self.browser = browser

    def input_login_credentials(self):
        username_input = self.browser.find_element(*self.USERNAME_INPUT)
        password_input = self.browser.find_element(*self.PASSWORD_INPUT)
        username_input.send_keys(self.USERNAME + Keys.TAB)
        password_input.send_keys(self.PASSWORD)

    def click_login_button(self):
        self.browser.find_element(*self.LOGIN_BUTTON).click()

    def user_login(self):
        self.input_login_credentials()
        self.click_login_button()