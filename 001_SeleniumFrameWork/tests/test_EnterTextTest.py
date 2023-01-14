import unittest
import pytest
import time
from pages.EnterTextPage import EnterText


@pytest.mark.usefixtures("beforeClass", "beforeMethod")
class EnterTextTest(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classObjects(self):
        self.et = EnterText(self.driver)

    @pytest.mark.run(order=4)
    def test_enterDataInEditBox(self):
        self.driver.maximize_window()
        time.sleep(2)
        self.et.enter_text()
        self.et.click_on_submit_button()

    @pytest.mark.run(order=3)
    def test_clickOnLocatorsPage(self):
        self.et.click_on_locators_page()
