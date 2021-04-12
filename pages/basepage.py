"""
This module contains BasePage,
the page object for all site-wide element/actions 
"""

from utils.wrapper import PageObject, HTMLElement, HTMLElementList


class BasePage:

    def __init__(self, browser):
        self.browser = browser

    def get_title(self):
        return self.browser.title

    def get_current_url(self):
        return self.browser.current_url