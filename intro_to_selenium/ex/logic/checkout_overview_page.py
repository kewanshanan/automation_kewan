from intro_to_selenium.ex.logic.checkout_page import CheckoutPage
from intro_to_selenium.ex.logic.inventory_page import InventoryPage


class CheckoutOverviewPage(CheckoutPage):
    ITEM_INFO = '//div[@class="inventory_item_name"]'
    CANCEL_CHECKOUT_BUTTON = '//button[@id="cancel"]'
    FINISH_CHECKOUT_BUTTON = '//button[@id="finish"]'
    def __init__(self, driver):
        super().__init__(driver)
        self._item_info = self._driver.find_element_by_xpath(self.ITEM_INFO)
        self._cancel_checkout_button = self._driver.find_element_by_xpath(self.CANCEL_CHECKOUT_BUTTON)
        self._finish_checkout_button = self._driver.find_element_by_xpath(self.FINISH_CHECKOUT_BUTTON)

    def item_info_button(self):
        self._item_info.click()
        return self._item_info

    def cancel_checkout_button(self):
        self._cancel_checkout_button.click()
        return InventoryPage

    def finish_checkout_button(self):
        self._finish_checkout_button.click()
