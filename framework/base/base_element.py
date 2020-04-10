from appium.webdriver.webelement import WebElement


class BaseElement:

    def __init__(self, web_element, name):
        self.web_element: WebElement = web_element
        self.name = name

    def is_visible(self) -> bool:
        return self.web_element.is_displayed()

    def click(self):
        self.web_element.click()

    def get_child_element_by_id(self, id_name):
        return self.web_element.find_element_by_id(id_name)

    def get_child_element(self, by, locator) -> WebElement:
        return self.web_element.find_element(by, locator)

    def get_text(self):
        return self.web_element.text
