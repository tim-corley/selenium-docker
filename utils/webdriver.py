import os
import json
import pytest
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from utils.logger import Logger, info

logger = Logger().get_logger()

class WebDriverInstance:

    def config(self):
        config_json = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'config.json')
        with open(config_json) as config_file:
            config = json.load(config_file)
        assert config['browser'] in ['Firefox Local', 'Firefox Remote', 'Chrome Local', 'Chrome Remote']
        assert isinstance(config['implicit_wait'], int)
        assert config['implicit_wait'] > 0
        return config

    def browser(self):
        config = self.config()
        if config['browser'] == 'Firefox Local':
            wd = webdriver.Firefox()
            wd.implicitly_wait(config['implicit_wait'])
            wd.maximize_window()
        elif config['browser'] == 'Firefox Remote':
            opts = webdriver.FirefoxOptions()
            opts.headless = True
            wd = webdriver.Remote(
            command_executor=(config['selenium_hub']),
            desired_capabilities = DesiredCapabilities.FIREFOX,
            options=opts)
        elif config['browser'] == 'Chrome Local':
            wd = webdriver.Chrome()
            wd.implicitly_wait(config['implicit_wait'])
            wd.maximize_window()
        elif config['browser'] == 'Chrome Remote':
            opts = webdriver.ChromeOptions()
            opts.add_argument('headless')
            wd = webdriver.Remote(config['selenium_hub'], opts.to_capabilities())
        else:
            error(logger, f'The browser is not supported.')
            # raise Exception(f'The "{config['browser']}" browser is not supported.')
        wd.get(config['target_url'])
        info(logger, 'initializing {} & fetching: {}'.format(config['browser'], config['target_url']))
        return wd

