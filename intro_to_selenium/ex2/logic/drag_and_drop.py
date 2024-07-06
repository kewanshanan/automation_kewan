from selenium.webdriver.common.by import By

from intro_to_selenium.ex2.logic.base_page_app_ import BasePageApp


class DragAndDrop(BasePageApp):
    COLUMN_A = '//div[@id="column-a"]'
    COLUMN_B = '//div[@id="column-b"]'
    def __init__(self, driver):
        super().__init__(driver)
        self._column_a = self._driver.find_element(By.XPATH,self.COLUMN_A)
        self._column_b = self._driver.find_element(By.XPATH,self.COLUMN_B)

    def drag(self):
        self._column_a.click()
