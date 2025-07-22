from behave import *
from selenium import webdriver

from pom.LoginPage import LoginPage
from utils.BasePage import DriverFactory
from utils.config_reader import ConfigReader

url = ConfigReader.get('default', 'base_url')
user_name = ConfigReader.get('default', 'username')
passcode = ConfigReader.get('default', 'password')

factory = DriverFactory()

@step
@given('login to application')
def loginToApplication(context):
    print('login to application')
    context.driver = factory.init_driver()
    login_page = LoginPage(context.driver)
    login_page.launch_browser(url)
    login_page.login(user_name, passcode)

@step
@when('user click on Home')
def openHomePage(context):
    context.driver.quit


def after_step(context, step):
    if step.status == "failed":
        screenshot = context.driver.get_screenshot_as_png()
        allure.attach(screenshot, name="screenshot", attachment_type=allure.attachment_type.PNG)
