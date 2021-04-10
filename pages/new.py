"""
This module contains NewPage,
the page object for Hacker News new page
"""

from pages.basepage import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class NewPage(BasePage):

    POST_TABLE = (By.CSS_SELECTOR, 'table.itemlist')
    POST_ROW = (By.TAG_NAME, 'tr')
    POST_DATA = (By.CSS_SELECTOR, 'td.subtext')
    POST_TIME = (By.CSS_SELECTOR, 'span.age')

    def __init__(self, browser):
        self.browser = browser

    def verify_posts_displayed(self):
        return self.browser.find_element(*self.POST_TABLE).is_displayed()

    def get_newest_post(self):
        table = self.browser.find_element(*self.POST_TABLE)
        rows = table.find_elements(*self.POST_ROW)
        return rows[:2]

    # returns true if post < 5 minutes old
    def verify_recent_post(self):
        subtext = self.get_newest_post()[1]
        subtext_data = subtext.find_element(*self.POST_DATA)
        data_age = subtext_data.find_element(*self.POST_TIME).text.split(' ')[0]
        print(f'\n\nPOST AGE: {data_age}')
        return int(data_age) < 5