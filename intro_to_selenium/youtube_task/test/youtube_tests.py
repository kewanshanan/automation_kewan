import unittest
from intro_to_selenium.youtube_task.infra.basepage import BasePage
from selenium.webdriver.common.by import By
from intro_to_selenium.youtube_task.infra.browser_wrapper import BrowserWrapper
from intro_to_selenium.youtube_task.infra.config_provider import ConfigProvider
from intro_to_selenium.youtube_task.logic.homepage import HomePage


class YoutubePageTest(unittest.TestCase):
    def setUp(self):
        self.browser = BrowserWrapper()
        self.config = ConfigProvider.load_config_json()
        self.driver = BrowserWrapper.get_driver(self.config["url"])
        self.base_page = BasePage(self.driver)
        self.home_page = HomePage(self.driver)
        self.home_page.search_input(self.config["SEARCH_INPUT"])
        
    def test_enter_with_chrome_browser(self):
        self.driver.get(self.config["url"])
        self.assertIn("YouTube", self.driver.title)
    
    def test_search_input(self):
        search_term = self.config["SEARCH_INPUT"]
        self.home_page.search_input(search_term)
        self.home_page.search_icon()
        search_box = self.driver.find_element(By.XPATH, HomePage.SEARCH_INPUT)
        self.assertEqual(search_box.get_attribute("value"), search_term)
    
    def test_video_history_button(self):
        self.home_page.burger_button()
        self.home_page.video_history_button()
        self.assertIn("video_history", self.driver.current_url)
    
    def test_liked_video_button(self):
        self.home_page.burger_button()
        self.home_page.liked_video_button()
        self.assertIn("liked_videos", self.driver.current_url)

    def test_choose_arabic_language(self):
        self.home_page.avatr_profile_button()
        self.home_page.change_language_button()
        self.home_page.choose_arabic_language()
        selected_language = self.driver.choose_arabic_language.is_displayed()
        self.assertTrue(selected_language)

    def tearDownClass(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
