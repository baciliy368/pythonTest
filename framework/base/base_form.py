from framework.utils.client_manager import ClientManager
from framework.utils.element_factory import get_label_by_id


class BaseForm:

    def __init__(self, __locator_of_page, __name):
        self.locator_of_page = __locator_of_page
        self.name = __name

    def is_form_opened(self):
        return get_label_by_id(self.locator_of_page, self.name).is_visible()
