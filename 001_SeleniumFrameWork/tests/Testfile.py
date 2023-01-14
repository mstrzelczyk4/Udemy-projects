from base.DriverClass import WebDriverClass
import time
from base.BasePage import BaseClass
from pages.ContactFormPage import ContactForm

wd = WebDriverClass()

driver = wd.get_web_driver("chrome")
bp = BaseClass(driver)
cf = ContactForm(driver)

bp.launch_web_page("http://www.dummypoint.com/seleniumtemplate.html", "Selenium Template")
#bp.sendText("Code2Lead", "user_input", "id")
#bp.clickOnElement("Form", "link")

#ele = bp.getWebElement("user_inpu", "id")
#ele.send_keys("code2lead")

#ele = bp.isElementDisplayed("user_input", "id")
#print(ele)
#bp.sendText("Code2Lead", "user_input", "id")

cf.click_contact_form()
time.sleep(2)
cf.verify_form_page()
cf.enter_name()
cf.enter_email()
cf.enter_message()
cf.enter_captcha()
cf.click_on_post_button()

time.sleep(2)
driver.quit()
