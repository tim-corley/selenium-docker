"""
This module contains PastPage,
the page object for Hacker News past page
"""

from datetime import datetime, timedelta
from utils.wrapper import PageObject, HTMLElement, HTMLElementList
from utils.logger import Logger, info, error

logger = Logger().get_logger()

class NavItem(HTMLElementList):
    nav_link = HTMLElement(tag_name='a')

class PastPage(PageObject):

    default_date = HTMLElement(xpath='//*[@id="hnmain"]/tbody/tr[3]/td/table/tbody/tr[2]/td[2]')
    links = NavItem(css='span.hnmore')

    def __init__(self, webdriver):
        self.webdriver = webdriver

    def get_date_shown(self):
        date_shown = self.default_date.text.split(' ')[2:5]
        return ' '.join([item for item in date_shown])

    # returns: Month ##, ####
    def get_yesterday(self):
        yesterday = datetime.now() - timedelta(1)
        return yesterday.strftime('%B %d, %Y')
    
    def get_previous_month(self):
        default_past_date = datetime.now() - timedelta(1)
        first_month_day = default_past_date.replace(day=1)
        previous_month = first_month_day - timedelta(1)
        last_month_date = datetime(previous_month.year, previous_month.month, default_past_date.day)
        return last_month_date.strftime('%B %d, %Y')

    def verify_yesterday_displayed(self):
        return self.get_date_shown() == self.get_yesterday()

    def verify_last_month_displayed(self):
        return self.get_date_shown() == self.get_previous_month()

    def navigate_past(self, increment):
        if increment == 'day':
            self.links[0].nav_link.click()
            info(logger, f'clicked {self.links[0].nav_link.text} link')
        elif increment == 'month':
            self.links[1].nav_link.click()
            info(logger, f'clicked {self.links[1].nav_link.text} link')
        elif increment == 'year':
            self.links[2].nav_link.click()
            info(logger, f'clicked {self.links[2].nav_link.text} link')
        else:
            error(logger, f'the time increment {increment} was not found')