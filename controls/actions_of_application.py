from unittest import TestCase

from controls.pages_of_application import *


def change_location(location_to_select):
    TestCase.assertTrue(start_screen_application_form().is_form_opened(), "Main form do not open")
    start_screen_application_form().click_location()
    locations_application_form().pass_notification_of_meeting()
    TestCase.assertTrue(locations_application_form().is_form_opened(), "Locations form do not open")
    locations_application_form().is_form_opened()
    locations_application_form().chose_location(location_to_select)
    TestCase.assertTrue(start_screen_application_form().is_form_opened(), "Main form do not open")
    TestCase.assertTrue(start_screen_application_form().get_location(), location_to_select, "Locations do match")


def open_first_discount_item():
    TestCase.assertTrue(start_screen_application_form().is_form_opened(), "Main Page do not open")
    btn_item = start_screen_application_form().get_first_discount_item()
    mdl_item_from_main_menu = start_screen_application_form().get_model_from_item(btn_item)
    btn_item.click()
    TestCase.assertTrue(item_application_form().is_form_opened(), "item application form do not open")
    mdl_item_from_item_page = item_application_form().get_model_from_form()
    TestCase().assertEqual(mdl_item_from_main_menu.brand, mdl_item_from_item_page.brand,
                           "Brands do not match")
    TestCase().assertEqual(mdl_item_from_item_page.priceNow, mdl_item_from_main_menu.priceNow,
                           "Current Prices do not match")
    TestCase().assertEqual(mdl_item_from_item_page.priceBeforeDiscount, mdl_item_from_main_menu.priceBeforeDiscount,
                           "Prices before discount do not match")
    TestCase().assertEqual(mdl_item_from_item_page.discount, mdl_item_from_main_menu.discount,
                           "Discounts do not match")


def open_seller_info_page():
    TestCase.assertTrue(item_application_form().is_form_opened(), "item application form do not open")
    seller_from_item_form = item_application_form().get_model_of_seller()
    item_application_form().open_seller_info()
    seller_info_form().is_form_opened()
    seller_from_seller_item_form = seller_info_form().get_seller_model()
    TestCase().assertEqual(seller_from_item_form.name, seller_from_seller_item_form.name,
                           "Seller's Names do not match")
    TestCase().assertEqual(seller_from_item_form.city, seller_from_seller_item_form.city,
                           "Seller's Cites do not match")