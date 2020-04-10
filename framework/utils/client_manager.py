import json

from appium import webdriver
from appium.common.logger import logger

from utils.config_reader import get_from_main_config


def configure_client():
    logger.info("Setting implicitlyWait")
    ClientManager().driver.implicitly_wait(get_from_main_config("implicitlyWait"))


def clean_client():
    logger.info("removing application")
    ClientManager().driver.remove_app(get_from_main_config("appId"))


class ClientManager:
    driver = None
    instance = None

    def __new__(cls):
        if cls.instance is None:
            cls.instance = super(ClientManager, cls).__new__(cls)
            cls.driver = cls.__install_application()
        return cls.instance

    @staticmethod
    def __install_application():
        logger.info("Reading config file")
        with open(get_from_main_config("clientConfigFilePath")) as json_client_file:
            data = json.load(json_client_file)
        logger.info("Installing app")
        return webdriver.Remote(get_from_main_config("connectionUrl"), data)
