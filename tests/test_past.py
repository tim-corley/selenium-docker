"""
These tests cover the Hacker News past page
"""

import pytest
from delayed_assert import expect, assert_expectations
from basetest import PastTest
from pages.past import PastPage


class TestPastPage(PastTest):

    def test_YesterdayDateDisplayed(self):
        past_page = PastPage(self.driver)
        expect(past_page.verify_yesterday_displayed())
        assert_expectations()