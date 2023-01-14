from base.BasePage import BaseClass
import utilities.CustomLogger as Cl


class ContactForm(BaseClass):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators  values in Contact form page

    _contactFromPage = "Form"  # link
    _formPage = "reused_form"  # id
    _enterName = "name"  # id
    _enterEmail = "email"  # id
    _enterMessage = "message"  # id
    _getCaptcha = "captcha_image"  # id
    _enterCaptcha = "captcha"  # id
    _postButton = "btnContactUs"  # id

    def click_contact_form(self):
        self.click_on_element(self._contactFromPage, "link")
        Cl.allure_logs("Clicked on Contact Form")

    def verify_form_page(self):
        element = self.is_element_displayed(self._formPage, "id")
        assert element
        Cl.allure_logs("Verified Contact Form")

    def enter_name(self):
        self.send_text("Code2Lead", self._enterName, "id")
        Cl.allure_logs("Entered Name")

    def enter_email(self):
        self.send_text("abc@gmail.com", self._enterEmail, "id")
        Cl.allure_logs("Entered Email")

    def enter_message(self):
        self.send_text("This is a Code2Lead", self._enterMessage, "id")
        Cl.allure_logs("Entered Message")

    def get_captcha(self):
        cap = self.get_text(self._getCaptcha, "id")
        Cl.allure_logs("Got the captcha data")
        return cap

    def enter_captcha(self):
        self.send_text(self.get_captcha(), self._enterCaptcha, "id")
        Cl.allure_logs("Entered captcha")

    def click_on_post_button(self):
        self.scroll_to(self._postButton, "id")
        self.click_on_element(self._postButton, "id")
        Cl.allure_logs("Clicked on the post button")
