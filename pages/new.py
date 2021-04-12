"""
This module contains NewPage,
the page object for Hacker News new page
"""

from utils.wrapper import PageObject, HTMLElement, HTMLElementList


class PostItem(HTMLElementList):
    post_age = HTMLElement(css='span.age')


class NewPage(PageObject):
    # gets all rows from posts table
    post_rows = PostItem(xpath='//*[@id="hnmain"]/tbody/tr[3]/td/table/tbody/tr')

    def __init__(self, webdriver):
        self.webdriver = webdriver

    def verify_posts_displayed(self):
        return self.post_table.is_displayed()

    # returns first two rows (header, subtitle) from the posts table
    def get_newest_post(self):
        return self.post_rows[:2]

    # returns true if post < 5 minutes old
    def verify_recent_post(self):
        subtext = self.get_newest_post()[1]
        data_age = subtext.post_age.text.split(' ')[0]
        return int(data_age) < 5

    # todo add a method that compares top post time vs. rest of posts
    # verify that top post time <= all others