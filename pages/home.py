"""
This module contains HomePage,
the page object for Hacker News home page
"""

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class HomePage:

    MENU_HEADER = (By.CSS_SELECTOR, 'b.hnname')
    POST_LISTING = (By.CSS_SELECTOR, 'table.itemlist')

    def __init__(self, browser):
        self.browser = browser

    def title(self):
        return self.browser.title

    def verify_menu_header_displayed(self):
        return self.browser.find_element(*self.MENU_HEADER).is_displayed()

    def verify_posts_displayed(self):
        return self.browser.find_element(*self.POST_LISTING).is_displayed()