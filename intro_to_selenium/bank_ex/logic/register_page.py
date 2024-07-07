from selenium.webdriver.common.by import By
from intro_to_selenium.bank_ex.infra.basepage import BasePage


class RegisterPage(BasePage):
    FIRST_NAME_INPUT = '//input[@id="customer.firstName"]'
    LAST_NAME_INPUT = '//input[@id="customer.lastName"]'
    ADDRESS_INPUT = '//input[@id="customer.address.street"]'
    CITY_INPUT = '//input[@id="customer.address.city"]'
    STATE_INPUT = '//input[@id="customer.address.state"]'
    ZIP_CODE_INPUT = '//input[@id="customer.address.zipCode"]'
    PHONE_INPUT = '//input[@id="customer.phoneNumber"]'
    SSN_INPUT = '//input[@id="customer.ssn"]'
    USER_NAME_INPUT = '//input[@id="customer.username"]'
    PASSWORD_INPUT = '//input[@id="customer.password"]'
    PASSWORD_CONFIRM_INPUT = '//input[@id="repeatedPassword"]'
    REGISTRATION_CONFIRM_BUTTON = '//input[@value="Register"]'

    def __init__(self, driver):
        super().__init__(driver)

    def first_name_input(self, first_name):
        self._driver.find_element(By.XPATH, self.FIRST_NAME_INPUT).send_keys(first_name)

    def last_name_input(self, last_name):
        self._driver.find_element(By.XPATH, self.LAST_NAME_INPUT).send_keys(last_name)

    def address_input(self, address):
        self._driver.find_element(By.XPATH, self.ADDRESS_INPUT).send_keys(address)

    def city_input(self, city):
        self._driver.find_element(By.XPATH, self.CITY_INPUT).send_keys(city)

    def state_input(self, state):
        self._driver.find_element(By.XPATH, self.STATE_INPUT).send_keys(state)

    def zip_code_input(self, zip_code):
        self._driver.find_element(By.XPATH, self.ZIP_CODE_INPUT).send_keys(zip_code)

    def phone_input(self, phone):
        self._driver.find_element(By.XPATH, self.PHONE_INPUT).send_keys(phone)

    def ssn_input(self, ssn):
        self._driver.find_element(By.XPATH, self.SSN_INPUT).send_keys(ssn)

    def user_name_input(self, user_name):
        self._driver.find_element(By.XPATH, self.USER_NAME_INPUT).send_keys(user_name)

    def password_input(self, password):
        self._driver.find_element(By.XPATH, self.PASSWORD_INPUT).send_keys(password)

    def password_confirm_input(self, password_confirm_input):
        self._driver.find_element(By.XPATH, self.PASSWORD_CONFIRM_INPUT).send_keys(password_confirm_input)

    def registration_confirm_button(self):
        self._driver.find_element(By.XPATH, self.REGISTRATION_CONFIRM_BUTTON).click()