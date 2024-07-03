from intro_to_selenium.ex.logic.cart_page import CartPage
from intro_to_selenium.ex.logic.checkout_overview_page import CheckoutOverviewPage


class CheckoutPage(CartPage):
    INPUT_FIRST_NAME = '//input[@id="first-name"]'
    INPUT_LAST_NAME = '//input[@id="last-name"]'
    INPUT_ZIP = '//input[@id="postal-code"]'
    CONTINUE_BUTTON = '//input[@id="continue"]'
    CANCEL_BUTTON = '//button[@id="cancel"]'

    def __init__(self, driver):
        super().__init__(driver)
        self._input_first_name = self._driver.find_element_by_id(self.INPUT_FIRST_NAME)
        self._input_last_name = self._driver.find_element_by_id(self.INPUT_LAST_NAME)
        self._input_zip = self._driver.find_element_by_id(self.INPUT_ZIP)
        self._continue_button = self._driver.find_element_by_id(self.CONTINUE_BUTTON)
        self._cancel_button = self._driver.find_element_by_id(self.CANCEL_BUTTON)

    def input_first_name(self, first_name):
        self._input_first_name.clear()
        self._input_first_name.send_keys(first_name)

    def input_last_name(self, last_name):
        self._input_last_name.clear()
        self._input_last_name.send_keys(last_name)

    def input_zip(self, zip):
        self._input_zip.clear()
        self._input_zip.send_keys(zip)

    def continue_button_click(self):
        self._continue_button.click()
        return CheckoutOverviewPage

    def cancel_button_click(self):
        self._cancel_button.click()
        return CartPage