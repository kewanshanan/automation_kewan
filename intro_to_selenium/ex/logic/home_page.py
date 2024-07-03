from selenium.webdriver.common.by import By
from intro_to_selenium.ex.infra.basepage import BasePage


class HomePage(BasePage):
    MAIN_LOGIN_LOGO = '//div[@class="login_logo"]'
    USERNAME_INPUT = '//input[@id="user-name"]'
    PASSWORD_INPUT = '//input[@id="password"]'
    LOGIN_BUTTON = '//input[@id="login-button"]'

    def __init__(self, driver):
        super().__init__(driver)
        self._main_login_logo = self._driver.find_element(By.XPATH, self.MAIN_LOGIN_LOGO)
        self._username_input = self._driver.find_element(By.XPATH, self.USERNAME_INPUT)
        self._password_input = self._driver.find_element(By.XPATH, self.PASSWORD_INPUT)
        self._login_button = self._driver.find_element(By.XPATH, self.LOGIN_BUTTON)

    def put_username_input(self, username):
        self._username_input.clear()
        self._username_input.send_keys(username)

    def put_password_input(self, password):
        self._password_input.clear()
        self._password_input.send_keys(password)

    def click_login_button(self):
        self._login_button.click()