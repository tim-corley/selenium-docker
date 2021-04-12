# -*- coding: UTF-8 -*-
import os
import json
import logging


class Style:

    def __init__(self):
        pass

    CYAN = '\033[36m'
    YELLOW = '\033[33m'
    BOLD = '\033[1m'
    RESET = '\033[0m'


class Logger:

    config_json = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'config.json')
    with open(config_json) as config_file:
        config = json.load(config_file)
    logger = logging.getLogger(config['log_file'])
    ch = logging.StreamHandler()
    fh = logging.FileHandler(config['log_file'])

    def __init__(self):
        self.logger.setLevel(logging.INFO)
        self.ch.setLevel(logging.INFO)

        formatter = logging.Formatter('%(asctime)s | %(levelname)s: %(message)s', datefmt='%Y-%m-%d %H:%M:%S')

        self.ch.setFormatter(formatter)
        self.fh.setLevel(logging.INFO)
        self.fh.setFormatter(formatter)

        self.logger.addHandler(self.ch)
        self.logger.addHandler(self.fh)

    def get_logger(self):
        return self.logger

def info(logger, message):
    logger.info((Style.CYAN + message + Style.RESET))

def error(logger, message):
    logger.error(Style.BOLD + Style.YELLOW + message + Style.RESET)