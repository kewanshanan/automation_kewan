from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from intro_to_selenium.ex.logic.base_page_app import BasePageAPP


class InventoryPage(BasePageAPP):
    ADD_TO_CART_BUTTON = '//button[@data-test="add-to-cart-sauce-labs-backpack"]'
    INVENTORY_ITEM_NAME = '//div[@class="inventory_item_name "]'
    INVENTORY_ITEM_IMG = '//img[@class="inventory_details_img"]'

    def __init__(self, driver):
        super().__init__(driver)
        self._add_to_cart_button = self._driver.find_element(By.XPATH, self.ADD_TO_CART_BUTTON)
        self._inventory_item_name = self._driver.find_element(By.XPATH, self.INVENTORY_ITEM_NAME)
        self._inventory_item_img = self._driver.find_element(By.XPATH, self.INVENTORY_ITEM_IMG)

    def click_add_to_cart_button(self):
        self._add_to_cart_button.click()

    def click_inventory_item_name(self):
        self._inventory_item_name.click()

    def click_inventory_item_img(self):
        self._inventory_item_img.click()
