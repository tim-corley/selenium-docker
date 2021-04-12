"""
This module contains HomePage,
the page object for Hacker News home page
"""

from utils.wrapper import PageObject, HTMLElement


class HomePage(PageObject):

    posts_table = HTMLElement(css='table.itemList')

    def __init__(self, webdriver):
        self.webdriver = webdriver

    def verify_posts_displayed(self):
        return self.posts_table.is_displayed()