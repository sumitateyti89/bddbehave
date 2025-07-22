from selenium.webdriver import Keys
from webdriver_manager.core import driver


class SeleniumActions:
    def __init__(self, driver):
        self.driver = driver

    def getElement(self, locator):
        return self.driver.find_element(*locator)

    def enterText(self, xpath, text):
        self.getElement(xpath).send_keys(text)

    def clickButton(self, xpath):
        self.getElement(xpath).click()

    def readText(self, xpath):
       return self.getElement(xpath).text()
