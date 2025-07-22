import time


from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from utils.Locators import LoginPageLocators, DashboardPageLocators

from utils.SeleniumActions import SeleniumActions


class LoginPage:

    def __init__(self, driver):
        self.driver = driver
        self.sel_action = SeleniumActions(driver)
        self.wait = WebDriverWait(driver, 10)

    def launch_browser(self, url):
        self.driver.get(url)
        self.driver.implicitly_wait(10)
        self.driver.set_page_load_timeout(10)
        time.sleep(10)

    def login(self, username, password):
        # import pdb;
        # pdb.set_trace()
        self.sel_action.enterText(LoginPageLocators.USERNAME_INPUT, username)
        time.sleep(10)
        self.sel_action.enterText(LoginPageLocators.PASSWORD_INPUT, password)
        self.sel_action.clickButton(LoginPageLocators.LOGIN_BUTTON)
        try:
            text = self.sel_action.readText(LoginPageLocators.PAGE_TITLE)
        except:
            self.driver.close()
            assert False, "Test Failed"

        if text == "Dashboard":
            assert True, "Test Passed" + text
