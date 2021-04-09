import os
import pytest
from selenium import webdriver
from utils.webdriver import WebDriverInstance


@pytest.fixture(scope='function')
def setup(request):
    wd = WebDriverInstance()
    driver = wd.browser()
    request.cls.driver = driver
    yield driver
    driver.quit()
