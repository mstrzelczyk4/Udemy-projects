import unittest
import pytest
import time
from base.BasePage import BaseClass
from pages.ContactFormPage import ContactForm


@pytest.mark.usefixtures("beforeClass", "beforeMethod")
class ContactFormTest(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classObjects(self):
        self.cf = ContactForm(self.driver)
        self.bp = BaseClass(self.driver)

    @pytest.mark.run(order=2)
    def test_enterDataInForm(self):
        time.sleep(5)
        self.cf.enter_name()
        self.cf.enter_email()
        self.cf.enter_message()
        self.cf.enter_captcha()
        self.cf.click_on_post_button()

    @pytest.mark.run(order=1)
    def test_formPage(self):
        self.cf.click_contact_form()
        self.cf.verify_form_page()
