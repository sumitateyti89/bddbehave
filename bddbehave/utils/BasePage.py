import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from utils.thread_local import thread_local


class DriverFactory:

    def init_driver(self):
        # Optional: Configure options
        options = webdriver.ChromeOptions()
        # options.add_argument("--start-maximized")

        # Create and return the driver
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
        driver.maximize_window()
        thread_local.driver = driver
        return driver


def get_driver():
    return getattr(thread_local, 'driver', None)


def quit_driver():
    driver = get_driver()
    if driver:
        driver.quit()
        thread_local.driver = None
