from framework.base.base_form import BaseForm
from framework.utils.element_factory import *
from models.application_selling_item import ApplicationSellingItem


class StartScreenForm(BaseForm):
    __id_location_button = 'tvToolbarCity'
    __id_of_items_in_ads_with_discount = "tvDiscount"
    __id_of_item_in_banner = "rlBanner"
    __id_of_brand_name = "tvBrand"
    __id_price_before_discount = "tvSumm"
    __id_price_after__discount = "tvPrice"
    __id_of_discount = "tvDiscount"

    def __init__(self):
        super().__init__("tvToolbarCity", "main page")

    def click_location(self):
        get_button_by_id(self.__id_location_button, "Location button").click()

    def get_location(self):
        return self.get_location_button().get_text()

    def get_location_button(self) -> Button:
        return get_button_by_id(self.__id_location_button, "Location button")

    def get_model_from_item(self, item_web_element: Button) -> ApplicationSellingItem:
        result_item = ApplicationSellingItem()
        result_item.brand = item_web_element.get_child_element_by_id(self.__id_of_brand_name).text
        result_item.priceNow = item_web_element.get_child_element_by_id(self.__id_price_after__discount).text
        result_item.priceBeforeDiscount = item_web_element.get_child_element_by_id(self.__id_price_before_discount).text
        result_item.discount = item_web_element.get_child_element_by_id(self.__id_of_discount).text
        return result_item

    def get_first_discount_item(self) -> Button:
        return get_buttons_by_id(self.__id_of_item_in_banner)[0]

    def open_first_item_from_ads_with_discount(self):
        get_button_by_id(self.__id_of_items_in_ads_with_discount, "item from banner").click()
