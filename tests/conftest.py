import os
import pytest
from selenium import webdriver
from utils.webdriver import WebDriverInstance
from pages.home import HomePage
from pages.login import LoginPage
from pages.nav import NavBar

@pytest.fixture(scope='function')
def setup(request):
    wd = WebDriverInstance()
    driver = wd.browser()
    request.cls.driver = driver
    yield driver
    driver.quit()

@pytest.fixture(scope='function')
def account_setup(request):
    wd = WebDriverInstance()
    driver = wd.browser()
    request.cls.driver = driver
    nav = NavBar(driver)
    login = LoginPage(driver)
    nav.click_login()
    login.user_login()
    yield driver
    nav.click_logout()
    driver.quit()

@pytest.fixture(scope='function')
def nav_new(request):
    nav = NavBar(request.cls.driver)
    nav.navigate_to_page('new')

@pytest.fixture(scope='function')
def nav_past(request):
    nav = NavBar(request.cls.driver)
    nav.navigate_to_page('past')

@pytest.fixture(scope='function')
def nav_comments(request):
    nav = NavBar(request.cls.driver)
    nav.navigate_to_page('comments')

@pytest.fixture(scope='function')
def nav_ask(request):
    nav = NavBar(request.cls.driver)
    nav.navigate_to_page('ask')

@pytest.fixture(scope='function')
def nav_show(request):
    nav = NavBar(request.cls.driver)
    nav.navigate_to_page('show')

@pytest.fixture(scope='function')
def nav_jobs(request):
    nav = NavBar(request.cls.driver)
    nav.navigate_to_page('jobs')

@pytest.fixture(scope='function')
def nav_submit(request):
    nav = NavBar(request.cls.driver)
    nav.navigate_to_page('submit')