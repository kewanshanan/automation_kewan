from pip._internal.resolution.resolvelib.factory import C
from selenium import webdriver
from intro_to_selenium.bank_ex.infra.config_provider import ConfigProvider


class BrowserWrapper:
    def __init__(self):
        self._driver = None
        self.config = ConfigProvider.load_config_json()

    def get_driver(self, url):
        try:
            if self.config["browser"] == "chrome":
                self._driver = webdriver.Chrome()
            elif self.config["browser"] == "firefox":
                self._driver = webdriver.Firefox()
            else:
                print("Browser type not supported")
                return None
            self._driver.get(url)
            return self._driver
        except C.webDriverException as e:
            print("ERROR : ", e)
            return None