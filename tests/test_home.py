"""
These tests cover the Hacker News homepage
"""

import pytest
from delayed_assert import expect, assert_expectations
from pages.home import HomePage

@pytest.mark.usefixtures("setup")
class TestLoggedoutHomepage():


    def test_HomepageLoads(self):
        home_page = HomePage(self.driver)
        expect(home_page.verify_menu_header_displayed())
        expect(home_page.verify_posts_displayed())
        assert_expectations()