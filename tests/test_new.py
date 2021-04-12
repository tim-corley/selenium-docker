"""
These tests cover the Hacker News new page
"""

import pytest
from delayed_assert import expect, assert_expectations
from basetest import UserNewTest
from pages.new import NewPage


class TestLoggedinNewPage(UserNewTest):

    def test_TopPostNewest(self):
        new_page = NewPage(self.driver)
        expect(new_page.verify_recent_post())
        assert_expectations()