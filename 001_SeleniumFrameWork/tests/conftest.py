import pytest
from base.BasePage import BaseClass
from base.DriverClass import WebDriverClass
import time


@pytest.fixture(scope='class')
def before_class(request):
    print('Before Class')
    driver1 = WebDriverClass()
    driver = driver1.get_web_driver("chrome")
    bp = BaseClass(driver)
    bp.launch_web_page("http://www.dummypoint.com/seleniumtemplate.html", "Selenium Template")
    if request.cls is not None:
        request.cls.driver = driver
    yield driver
    time.sleep(5)
    driver.quit()
    print('After Class')


@pytest.fixture()
def before_method():
    print('Before Method')
    yield
    print('After Method')
