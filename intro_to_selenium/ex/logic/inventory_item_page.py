from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from intro_to_selenium.ex.logic.base_page_app import BasePageAPP
from intro_to_selenium.ex.logic.inventory_page import InventoryPage


class InventoryItemPage(InventoryPage):
    ITEM_NAME = '//div[@class="inventory_details_name large_size"]'
    ITEM_IMAGE = '//img[@class="inventory_details_img"]'
    ADD_TO_CART_BUTT = '//button[@id="add-to-cart"]'
    BACK_TO_PRODUCTS_BUTTON = '//button[@id="back-to-products"]'

    def __init__(self, driver):
        super().__init__(driver)
        self._item_name = self._driver.find_element_by_xpath(self.ITEM_NAME)
        self._item_image = self._driver.find_element_by_xpath(self.ITEM_IMAGE)
        self._add_to_cart_butt = self._driver.find_element_by_xpath(self.ADD_TO_CART_BUTT)
        self._back_to_products_button = self._driver.find_element_by_xpath(self.BACK_TO_PRODUCTS_BUTTON)

    def click_add_to_cart_button(self):
        self._add_to_cart_butt.click()

    def click_back_to_products_button(self):
        self._back_to_products_button.click()


