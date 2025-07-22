from selenium.webdriver.common.by import By

class LoginPageLocators:
    USERNAME_INPUT = (By.XPATH, "//input[@name='username']")
    PASSWORD_INPUT = (By.XPATH, "//input[@name='password']")
    LOGIN_BUTTON   = (By.XPATH, "//button[@type='submit']")
    PAGE_TITLE = (By.XPATH, "//div[@class='oxd-topbar-header']//h6")

class DashboardPageLocators:
    WELCOME_MESSAGE = (By.XPATH, "//div[@class='welcome']")
