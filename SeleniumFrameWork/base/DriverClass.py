from selenium import webdriver
import utilities.CustomLogger as Cl
from selenium.webdriver.chrome.service import Service


class WebDriverClass:
    log = Cl.custom_logger()

    def get_web_driver(self, browser_name):
        driver = None
        if browser_name == "chrome":
            driver = webdriver.Chrome(service=Service("C:/development/drivers/chromedriver"))
            self.log.info("Chrome Driver is initializing")
        elif browser_name == "safari":
            driver = webdriver.Safari()
            self.log.info("Safari Driver is initializing")
        elif browser_name == "firefox":
            driver = webdriver.Firefox(service=Service("C:/development/drivers/geckodriver"))
            self.log.info("FireFox Driver is initializing")

        return driver
