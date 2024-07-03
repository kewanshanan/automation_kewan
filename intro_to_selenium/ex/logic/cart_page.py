from intro_to_selenium.ex.logic.checkout_page import CheckoutPage
from intro_to_selenium.ex.logic.inventory_page import InventoryPage
from intro_to_selenium.ex.logic.inventory_item_page import InventoryItemPage


class CartPage(InventoryItemPage):
    ITEM_NAME_BUTTON = '//div[@class="inventory_item_name"]'
    REMOVE_ITEM_BUTTON = '//button[@class="btn btn_secondary btn_small cart_button"]'
    CONTINUE_SHOPPING_BUTTON = '//button[@class="btn btn_secondary back btn_medium"]'
    CHECKOUT_BUTTON = '//button[@class="btn btn_action btn_medium checkout_button "]'
    def __init__(self, driver):
        super().__init__(driver)
        self._item_name_button = self._driver.find_element_by_xpath(self.ITEM_NAME_BUTTON)
        self._remove_item_button = self._driver.find_element_by_xpath(self.REMOVE_ITEM_BUTTON)
        self._continue_shopping_button = self._driver.find_element_by_xpath(self.CONTINUE_SHOPPING_BUTTON)
        self._checkout_button = self._driver.find_element_by_xpath(self.CHECKOUT_BUTTON)

    def click_item_name(self):
        self._item_name_button.click()

    def click_remove_item(self):
        self._remove_item_button.click()

    def click_continue_shopping(self):
        self._continue_shopping_button.click()
        return InventoryPage

    def click_checkout_button(self):
        self._checkout_button.click()
        return CheckoutPage

    def get_cart_count(self):
        pass