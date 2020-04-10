from pages.item_form import ItemForm
from pages.item_seller_form import ItemSellerForm
from pages.locations_form import LocationsForm
from pages.main_form import StartScreenForm


def start_screen_application_form() -> StartScreenForm:
    return StartScreenForm()


def locations_application_form() -> LocationsForm:
    return LocationsForm()


def item_application_form() -> ItemForm:
    return ItemForm()


def seller_info_form() -> ItemSellerForm:
    return ItemSellerForm()
