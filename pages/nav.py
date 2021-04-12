"""
This module contains NavBar,
the page object for Hacker News top navigation bar component
"""

import os
from dotenv import load_dotenv
from utils.wrapper import PageObject, HTMLElement



class NavBar(PageObject):
    load_dotenv()
    menu_header = HTMLElement(css='b.hnname')
    login_link = HTMLElement(css='a[href="login?goto=news"]')
    logout_link = HTMLElement(id_='logout')
    username_link = HTMLElement(id_='me')
    nav_home = HTMLElement(css='a[href="news"]')
    nav_new = HTMLElement(css='a[href="newest"]')
    nav_past = HTMLElement(css='a[href="front"]')
    nav_comments = HTMLElement(css='a[href="newcomments"]')
    nav_ask = HTMLElement(css='a[href="ask"]')
    nav_show = HTMLElement(css='a[href="show"]')
    nav_jobs = HTMLElement(css='a[href="jobs"]')
    nav_submit = HTMLElement(css='a[href="submit"]')
    USERNAME = os.getenv('USERNAME')

    def __init__(self, webdriver):
        self.webdriver = webdriver

    def verify_menu_header_displayed(self):
        return self.menu_header.is_displayed()

    def verify_username_displayed(self):
        return self.username_link.is_displayed() and self.username_link.text == self.USERNAME

    def click_login(self):
        self.login_link.click()

    def click_logout(self):
        self.logout_link.click()

    # select item
    def navigate_to_page(self, page):
        if page == 'home':
            self.nav_home.click()
        elif page == 'new':
            self.nav_new.click()
        elif page == 'past':
            self.nav_past.click()
        elif page == 'comments':
            self.nav_comments.click()
        elif page == 'ask':
            self.nav_ask.click()
        elif page == 'show':
            self.nav_show.click()
        elif page == 'jobs':
            self.nav_jobs.click()
        elif page == 'submit':
            self.nav_submit.click()
        elif page == 'login':
            self.login_link.click()
        else:
            print('no page found.')
