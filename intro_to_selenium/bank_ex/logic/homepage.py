from selenium.webdriver.common.by import By
from intro_to_selenium.bank_ex.infra.basepage import BasePage


class HomePage(BasePage):
    REGISTER_BUTTON = '//*[@id="loginPanel"]/p[2]/a'

    def __init__(self,driver):
        super().__init__(driver)
        self._register_button = self._driver.find_element(By.XPATH, self.REGISTER_BUTTON)

    def register_button(self):
        self._register_button.click()