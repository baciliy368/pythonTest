from framework.base.base_element import BaseElement


class TextField(BaseElement):

    def __init__(self, web_element, name):
        super().__init__(web_element, name)

    def type(self, text):
        self.web_element.set_text(text)

