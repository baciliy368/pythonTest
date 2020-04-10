from framework.base.base_form import BaseForm
from framework.utils.element_factory import *
from models.aaplication_item_seller import ApplicationItemSeller
from models.application_selling_item import ApplicationSellingItem


class ItemForm(BaseForm):
    __id_brand_name = "tvItemBrand"
    __id_price_before_discount = "tvItemOriginalPrice"
    __id_price_after__discount = "tvItemPrice"
    __id_discount = "tvItemDiscount"
    __id_seller_avatar = "ivSellerAvatar"
    __id_name_of_seller = "tvItemSellerName"
    __id_city_of_seller = "tvItemSellerCity"

    def __init__(self):
        super().__init__("ivSellerAvatar", "main page")

    def get_model_from_form(self) -> ApplicationSellingItem:
        result_item = ApplicationSellingItem()
        result_item.brand = get_label_by_id(self.__id_brand_name, "Brand name").get_text()
        result_item.priceBeforeDiscount = get_label_by_id(self.__id_price_before_discount, "Price before").get_text()
        result_item.priceNow = get_label_by_id(self.__id_price_after__discount, "Price now").get_text()
        result_item.discount = get_label_by_id(self.__id_discount, "Price now").get_text()
        return result_item

    def open_seller_info(self):
        get_button_by_id(self.__id_seller_avatar, "seller avatar").click()

    def get_model_of_seller(self):
        result_item = ApplicationItemSeller()
        result_item.name = get_label_by_id(self.__id_name_of_seller, "seller name").get_text()
        result_item.city = get_label_by_id(self.__id_city_of_seller, "seller city").get_text()
        return result_item
