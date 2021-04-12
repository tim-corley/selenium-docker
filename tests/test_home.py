"""
These tests cover the Hacker News homepage
"""

import pytest
from delayed_assert import expect, assert_expectations
from basetest import HomeTest, LoggedInTest
from pages.home import HomePage
from pages.nav import NavBar


class TestLoggedoutHomepage(HomeTest):


    def test_HomepageLoadsLoggedOut(self):
        nav = NavBar(self.driver)
        home_page = HomePage(self.driver)
        expect(nav.verify_menu_header_displayed())
        expect(home_page.verify_posts_displayed())
        assert_expectations()


class TestLoggedinHomepage(LoggedInTest):

    def test_HomepageLoadsLoggedIn(self):
        nav = NavBar(self.driver)
        home_page = HomePage(self.driver)
        expect(nav.verify_username_displayed())
        expect(nav.verify_menu_header_displayed())
        expect(home_page.verify_posts_displayed())
        assert_expectations()