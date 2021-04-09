import os
import json
import pytest
from selenium import webdriver

class WebDriverInstance:

    def config(self):
        config_json = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'config.json')
        with open(config_json) as config_file:
            config = json.load(config_file)
        assert config['browser'] in ['Firefox', 'Firefox Headless', 'Chrome', 'Headless Chrome']
        assert isinstance(config['implicit_wait'], int)
        assert config['implicit_wait'] > 0
        return config


    def browser(self):
        config = self.config()
        if config['browser'] == 'Firefox':
            wd = webdriver.Firefox()
        elif config['browser'] == 'Firefox Headless':
            opts = webdriver.FirefoxOptions()
            opts.headless = True
            wd = webdriver.Firefox(options=opts)
        elif config['browser'] == 'Chrome':
            wd = webdriver.Chrome()
        elif config['browser'] == 'Headless Chrome':
            opts = webdriver.ChromeOptions()
            opts.add_argument('headless')
            wd = webdriver.Chrome(options=opts)
        else:
            raise Exception(f'The "{config["browser"]}" browser is not supported')
        wd.implicitly_wait(config['implicit_wait'])
        wd.maximize_window()
        wd.get(config['target_url'])
        return wd

