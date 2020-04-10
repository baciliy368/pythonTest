from framework.base.base_test import BaseTestCase
import controls.actions_of_application as actions
from utils.config_reader import get_from_main_config


class Test(BaseTestCase):
    city_for_search = get_from_main_config("cityForSearch")

    def test_first(self):
        actions.change_location(self.city_for_search)
        actions.open_first_discount_item()
        actions.open_seller_info_page()
