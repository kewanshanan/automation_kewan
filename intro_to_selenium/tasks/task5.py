from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys

# def select_test():
#     driver = webdriver.Chrome()
#     try:
#         # Navigate to the page with the drop-down list
#         driver.get("https://www.amazon.com/")
#
#         # Find the drop-down list element by ID
#         dropdown = driver.find_element(By.ID, "searchDropdownBox")
#
#         # Create a Select object
#         select = Select(dropdown)
#
#         # Select the "Books" option
#         select.select_by_value("search-alias=stripbooks-intl-ship")
#         select.send_keys("coloring book")
#         select.send_keys(Keys.ENTER)
#
#     finally:
#         # Close the browser after the operations
#         driver.quit()


# Run the test function
# select_test()
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import Select
# import unittest
#
#
# class TestCombined(unittest.TestCase):
#     def setUp(self):
#         self.driver = webdriver.Chrome()
#         self.driver.implicitly_wait(10)
#
#     def test_select(self):
#         self.driver = webdriver.Chrome()
#         # Navigate to the page with the drop-down list
#         self.driver.get("https://www.amazon.com/")
#
#         # Find the drop-down list element by ID
#         dropdown = self.driver.find_element(By.ID, "searchDropdownBox")
#
#         # Create a Select object
#         select = Select(dropdown)
#
#         # Select the "Books" option
#         select.select_by_value("search-alias=stripbooks-intl-ship")
#
#     def tearDown(self):
#         self.driver.quit()
