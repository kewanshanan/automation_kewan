import unittest
from selenium import webdriver
from intro_to_selenium.ex.logic.login_page import LoginPage
from intro_to_selenium.ex.logic.home_page import HomePage
from intro_to_selenium.ex.logic.cart_page import CartPage

class TestSauceDemo(unittest.TestCase):
    def __init__(self, methodName: str = "runTest"):
        super().__init__(methodName)
        self._add_to_cart_butt = None

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get('https://www.saucedemo.com/')
        self._login_page = LoginPage(self.driver)
        self._home_page = HomePage(self.driver)
        self._cart_page = CartPage(self.driver)

    def test_login_add_2_items_validate_cart(self):
        self._login_page._login_button('standard_user', 'secret_sauce')
        self._cart_page._add_to_cart_butt([0, 1])
        self.assertEqual(self._cart_page.get_cart_count(), 2)

    def test_login_add_3_items_remove_1_validate_cart(self):
        self._login_page._login_button('standard_user', 'secret_sauce')
        self._cart_page._add_to_cart_butt([0, 1, 2])
        self._cart_page._add_to_cart_butt.click()
        self._add_to_cart_butt.remove_item(0)
        self.assertEqual(self._add_to_cart_butt.get_cart_item_count(), 2)

    def test_custom_flow(self):
        self._login_page._login_button('standard_user', 'secret_sauce')
        self._cart_page._add_to_cart_butt([0, 2])
        self._cart_page._cart_button.click()
        self.assertEqual(self._cart_page.get_cart_count(), 2)

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
