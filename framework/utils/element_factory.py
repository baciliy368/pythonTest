import json
from appium.common.logger import logger
from selenium.webdriver.common.by import By
from framework.elements.button import Button
from framework.elements.label import Label
from framework.elements.text_field import TextField
from framework.utils.client_manager import ClientManager

__pattern_id_with_app_id = "%s:id/%s"


def get_button_by_id(id_name, name) -> Button:
    logger.info("searching element with %s id and name %s" % (id_name, name))
    return Button(ClientManager().driver.find_element_by_id(__get_id_with_add_id(id_name)), name)


def get_button_by_id_without_app_id(id_name, name) -> Button:
    logger.info("searching element with %s id and name %s" % (id_name, name))
    return Button(ClientManager().driver.find_element_by_id(id_name), name)


def __get_id_with_add_id(id_name):
    with open('../resources/test_config.json') as json_file:
        main_conf = json.load(json_file)
        return __pattern_id_with_app_id % (main_conf["appId"], id_name)


def __get_elements_by_id(id_name) -> list:
    logger.info("searching elements with %s id" % id_name)
    return ClientManager().driver.find_elements_by_id(__get_id_with_add_id(id_name))


def get_text_field_by_id(id_name, name) -> TextField:
    logger.info("searching element with %s id and name %s" % (id_name, name))
    return TextField(ClientManager().driver.find_element_by_id(__get_id_with_add_id(id_name)), name)


def get_label_by_id(id_name, name) -> Label:
    logger.info("searching label with %s id and name %s" % (id_name, name))
    return Label(ClientManager().driver.find_element_by_id(__get_id_with_add_id(id_name)), name)


def get_label_by_xpath(locator, name) -> Label:
    logger.info("searching label with %s xpath and name %s" % (locator, name))
    return Label(ClientManager().driver.find_element(By.XPATH, locator), name)


def get_buttons_by_id(id_name) -> list:
    logger.info("searching buttons with %s id" % id_name)
    result = __get_elements_by_id(id_name)
    result = [Button(i, "Element in list") for i in result]
    return result
