"""
This module contains NavBar,
the page object for Hacker News top navigation bar component
"""

import os
from dotenv import load_dotenv
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class NavBar:

    load_dotenv()
    USERNAME = os.getenv('USERNAME')
    MENU_HEADER = (By.CSS_SELECTOR, 'b.hnname')
    LOGIN_LINK = (By.CSS_SELECTOR, 'a[href="login?goto=news"]')
    LOGOUT_LINK = (By.ID, 'logout')
    USERNAME_LINK = (By.ID, 'me')
    NAV_HOME = (By.CSS_SELECTOR, 'a[href="news"]')
    NAV_NEW = (By.CSS_SELECTOR, 'a[href="newest"]')
    NAV_PAST = (By.CSS_SELECTOR, 'a[href="front"]')
    NAV_COMMENTS = (By.CSS_SELECTOR, 'a[href="newcomments"]')
    NAV_ASK = (By.CSS_SELECTOR, 'a[href="ask"]')
    NAV_SHOW = (By.CSS_SELECTOR, 'a[href="show"]')
    NAV_JOBS = (By.CSS_SELECTOR, 'a[href="jobs"]')
    NAV_SUBMIT = (By.CSS_SELECTOR, 'a[href="submit"]')

    def __init__(self, browser):
        self.browser = browser

    def verify_menu_header_displayed(self):
        return self.browser.find_element(*self.MENU_HEADER).is_displayed()

    def verify_username_displayed(self):
        return self.browser.find_element(*self.USERNAME_LINK).is_displayed() and self.browser.find_element(*self.USERNAME_LINK).text == self.USERNAME

    def click_login(self):
        self.browser.find_element(*self.LOGIN_LINK).click()

    def click_logout(self):
        self.browser.find_element(*self.LOGOUT_LINK).click()

    # select item
    def navigate_to_page(self, page):
        if page == 'home':
            self.browser.find_element(*self.NAV_HOME).click()
        elif page == 'new':
            self.browser.find_element(*self.NAV_NEW).click()
        elif page == 'past':
            self.browser.find_element(*self.NAV_PAST).click()
        elif page == 'comments':
            self.browser.find_element(*self.NAV_COMMENTS).click()
        elif page == 'ask':
            self.browser.find_element(*self.NAV_ASK).click()
        elif page == 'show':
            self.browser.find_element(*self.NAV_SHOW).click()
        elif page == 'jobs':
            self.browser.find_element(*self.NAV_JOBS).click()
        elif page == 'submit':
            self.browser.find_element(*self.NAV_SUBMIT).click()
        elif page == 'login':
            self.browser.find_element(*self.LOGIN_LINK).click()
        else:
            print('no page found.')
