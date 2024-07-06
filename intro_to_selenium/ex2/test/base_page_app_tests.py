import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from intro_to_selenium.ex2.logic.add_remove_elements import AddRemoveElements
from intro_to_selenium.ex2.logic.broken_images import BrokenImages
from intro_to_selenium.ex2.logic.challenging_dom import ChallengingDOM
from intro_to_selenium.ex2.logic.check_box import CheckBoxes
from intro_to_selenium.ex2.logic.context_menu import ContextMenu


class TestCombined(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    # def test_add_remove_elements(self):
    #     self.driver.get('https://the-internet.herokuapp.com/add_remove_elements/')
    #     page = AddRemoveElements(self.driver)
    #     # הוספת שני כפתורים
    #     page.add_element()
    #     page.add_element()
    #     # וידוא שיש שני כפתורי מחיקה
    #     delete_buttons = self.driver.find_elements(By.XPATH, AddRemoveElements.DELETE_ELEMENT)
    #     self.assertEqual(len(delete_buttons), 2)
    #     # מחיקת כפתור אחד
    #     page.delete_element(0)
    #     # וידוא שנשאר כפתור מחיקה אחד
    #     delete_buttons = self.driver.find_elements(By.XPATH, AddRemoveElements.DELETE_ELEMENT)
    #     self.assertEqual(len(delete_buttons), 1)
    #
    # def test_broken_images(self):
    #     self.driver.get('https://the-internet.herokuapp.com/broken_images')
    #     page = BrokenImages(self.driver)
    #
    #     # בדיקת התמונות
    #     results = page.validate_images()
    #     print(results)
    #
    #     # ציפיות בהתאם למצב התמונות באתר
    #     expected_results = {
    #         'first_broken_image': True,
    #         'second_broken_image': True,
    #         'avatar_blank_image': False
    #     }
    #     self.assertEqual(results, expected_results)
    #
    #
    # def test_challenging_dom(self):
    #     self.driver.get('https://the-internet.herokuapp.com/challenging_dom')
    #     page = ChallengingDOM(self.driver)
    #
    #     # בדיקה של לחיצה על כל הכפתורים
    #     for i in range(3):
    #         page.click_button(i)
    #         # וידוא שהלחיצה עברה בהצלחה על ידי כך שאין שגיאה
    #         self.assertTrue(True)
    #
    #     # בדיקת נוכחות של הטבלה
    #     table_text = page.get_table_text()
    #     self.assertTrue(len(table_text) > 0)
    #
    #     # בדיקת נוכחות של ה-Canvas
    #     self.assertTrue(page.is_canvas_present())


    # def test_checkboxes(self):
    #     self.driver.get('https://the-internet.herokuapp.com/checkboxes')
    #     page = CheckBoxes(self.driver)
    #
    #     # Click the first checkbox
    #     page.click_check_box_1()
    #     check_box_1 = self.driver.find_element(*CheckBoxes.CHECK_BOX_1)
    #     self.assertTrue(check_box_1.is_selected())
    #
    #     # Click the second checkbox
    #     page.click_check_box_2()
    #     check_box_2 = self.driver.find_element(*CheckBoxes.CHECK_BOX_2)
    #     self.assertFalse(check_box_2.is_selected())
    #
    #     # Double click the first checkbox to uncheck it
    #     page.double_click_check_box_1()
    #     self.assertTrue(check_box_1.is_selected())
    #     print("checkboxes test passed")

    def test_contex_menu(self):
        self.driver.get('https://the-internet.herokuapp.com/context_menu')
        page = ContextMenu(self.driver)
        page.right_click_in_hot_spot()
        alert = self.driver.switch_to.alert
        self.assertEqual(alert.text, "You selected a context menu")
        alert.accept()
        print("context menu test passed")
    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
