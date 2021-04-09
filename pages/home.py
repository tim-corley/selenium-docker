"""
This module contains HomePage,
the page object for Hacker News home page
"""

from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class HomePage(BasePage):

    POST_LISTING = (By.CSS_SELECTOR, 'table.itemlist')

    def __init__(self, browser):
        self.browser = browser

    def verify_posts_displayed(self):
        return self.browser.find_element(*self.POST_LISTING).is_displayed()