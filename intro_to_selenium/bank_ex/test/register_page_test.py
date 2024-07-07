import unittest
from selenium.webdriver.common.by import By
from intro_to_selenium.bank_ex.infra.browser_wrapper import BrowserWrapper
from intro_to_selenium.bank_ex.infra.config_provider import ConfigProvider
from intro_to_selenium.bank_ex.logic.homepage import HomePage
from intro_to_selenium.bank_ex.logic.register_page import RegisterPage


class RegisterPageTest(unittest.TestCase):
    def setUp(self):
        self.browser = BrowserWrapper()
        self.config = ConfigProvider.load_config_json()
        self.driver = self.browser.get_driver(self.config["url"])
        self.home_page = HomePage(self.driver)
        self.register_page = RegisterPage(self.driver)

    def test_register_page_successfully(self):
        self.home_page.register_button()
        self.register_page.first_name_input(self.config["FIRST_NAME_INPUT"])
        self.register_page.last_name_input(self.config["LAST_NAME_INPUT"])
        self.register_page.address_input(self.config["ADDRESS_INPUT"])
        self.register_page.city_input(self.config["CITY_INPUT"])
        self.register_page.state_input(self.config["STATE_INPUT"])
        self.register_page.zip_code_input(self.config["ZIP_CODE_INPUT"])
        self.register_page.phone_input(self.config["PHONE_NUMBER_INPUT"])
        self.register_page.ssn_input(self.config["SSN_INPUT"])
        self.register_page.user_name_input(self.config["USER_NAME_INPUT"])
        self.register_page.password_input(self.config["PASSWORD_INPUT"])
        self.register_page.password_confirm_input(self.config["PASSWORD_CONFIRM_INPUT"])
        self.register_page.registration_confirm_button()

        success_message = self.driver.find_element(By.XPATH, '//h1[@class="title"]')
        self.assertTrue(success_message.is_displayed(), "Registration was successful")

        print("test passed")


    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()