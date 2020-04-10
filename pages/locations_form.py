from framework.base.base_form import BaseForm
from framework.utils.element_factory import *


class LocationsForm(BaseForm):
    __id_location_textfield = 'etSearchTest'
    __id_of_OK_button_in_notification = "android:id/button1"
    __locator_of_location = "//android.widget.TextView[@text='%s']"

    def __init__(self):
        super().__init__("tvAction", "Locations page")

    def pass_notification_of_meeting(self):
        get_button_by_id_without_app_id(self.__id_of_OK_button_in_notification, "OK button").click()

    def chose_location(self, text_of_location):
        get_text_field_by_id(self.__id_location_textfield, "Location text field").type(text_of_location)
        get_label_by_xpath(self.__locator_of_location % text_of_location, "Location button").click()

