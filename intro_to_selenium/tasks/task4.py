from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

class DragAndDrop:
    ACECARD = '//div[@id="card13"]'
    FOUNZERO = '//img[@id="foun0"]'
    def __init__(self, driver):
        self.driver = driver
        super().__init__(driver)
        self.acecard = self.driver.find_element(By.XPATH, self.ACECARD)
        self.foundzero = self.driver.find_element(By.XPATH, self.FOUNZERO)

    # def test_darg_andd_rop(self):
        driver = webdriver.Chrome()
        driver.get("https://www.solnet.co.il/klondike3")
        actions = ActionChains(self.driver)
        actions.drag_and_drop(self.acecard, self.foundzero)
