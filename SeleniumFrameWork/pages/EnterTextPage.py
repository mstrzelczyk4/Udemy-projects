from base.BasePage import BaseClass
import utilities.CustomLogger as Cl


class EnterText(BaseClass):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators values in Contact form
    _locatorsPage = "Locators" # link
    _enterTextEditBox = "user_input"  # id
    _submitButton = "submitbutton"  # id

    def click_on_locators_page(self):
        self.click_on_element(self._locatorsPage, "link")

    def enter_text(self):
        self.send_text("Code2Lead", self._enterTextEditBox, "id")
        Cl.allure_logs("Entered Text in Edit Box")

    def click_on_submit_button(self):
        self.click_on_element(self._submitButton, "id")
