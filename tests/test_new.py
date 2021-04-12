"""
These tests cover the Hacker News new page
"""

import pytest
from delayed_assert import expect, assert_expectations
from basetest import NewTest
from pages.new import NewPage


class TestNewPage(NewTest):

    def test_TopPostNewest(self):
        new_page = NewPage(self.driver)
        expect(new_page.verify_recent_post())
        assert_expectations()