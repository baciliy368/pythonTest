from framework.base.base_form import BaseForm
from framework.utils.element_factory import *
from models.aaplication_item_seller import ApplicationItemSeller


class ItemSellerForm(BaseForm):
    __locator_seller_name = "//android.view.ViewGroup/android.widget.TextView"
    __id_city = "tvItemSellerCity"

    def __init__(self):
        super().__init__("lvSellerItems", "Seller info form")

    def __get_seller_name(self):
        return get_label_by_xpath(self.__locator_seller_name, "name of seller").get_text()

    def get_seller_model(self):
        result_seller = ApplicationItemSeller()
        result_seller.name = self.__get_seller_name()
        result_seller.city = self.__get_city()
        return result_seller

    def __get_city(self):
        return get_label_by_id(self.__id_city, "city").get_text()

