"""
This module contains PastPage,
the page object for Hacker News past page
"""

from datetime import datetime, timedelta
from utils.wrapper import PageObject, HTMLElement


class PastPage(PageObject):
    # gets all rows from posts table
    default_date = HTMLElement(xpath='//*[@id="hnmain"]/tbody/tr[3]/td/table/tbody/tr[2]/td[2]')

    def __init__(self, webdriver):
        self.webdriver = webdriver

    # returns: Month ##, ####
    def get_yesterday(self):
        yesterday = datetime.now() - timedelta(1)
        return yesterday.strftime('%B %d, %Y')

    def verify_yesterday_displayed(self):
        date_shown = self.default_date.text.split(' ')[2:5]
        formatted_date = ' '.join([item for item in date_shown])
        expected_date = self.get_yesterday()
        return formatted_date == expected_date