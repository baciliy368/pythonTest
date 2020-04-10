import json
from appium.common.logger import logger


def get_from_main_config(key):
    with open('../resources/test_config.json') as json_file:
        main_conf = json.load(json_file)
        logger.info("reading from main config")
        return main_conf[key]

