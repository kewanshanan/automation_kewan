from intro_to_selenium.ex.logic.checkout_overview_page import CheckoutOverviewPage
from intro_to_selenium.ex.logic.inventory_page import InventoryPage


class CheckoutComplete(CheckoutOverviewPage):
    COMPLETE_ORDER = '//div[@id="checkout_complete_container"]'
    BACK_HOME_BUTTON = '//button[@id="back-to-products"]'

    def __init__(self, driver):
        super().__init__(driver)
        self._complete_order = self._driver.find_element_by_xpath(self.COMPLETE_ORDER)
        self._back_home_button = self._driver.find_element_by_xpath(self.BACK_HOME_BUTTON)

    def get_complete_order(self):
        return self._complete_order.get_attribute('innerHTML')

    def get_back_home_button(self):
        self._back_home_button.click()
        return InventoryPage
