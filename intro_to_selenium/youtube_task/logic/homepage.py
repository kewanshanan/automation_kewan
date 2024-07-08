from selenium.webdriver.common.by import By
from intro_to_selenium.youtube_task.infra.basepage import BasePage
from selenium.common import exceptions as c


class HomePage(BasePage):
    try:
        # YOUTUBE_LOGO = '//ytd-masthead//a[@class="yt-simple-endpoint style-scope ytd-topbar-logo-renderer"]'
        SEARCH_INPUT = '//input[@id="search"]'
        SEARCH_ICON = '//button[@id="search-icon-legacy"]'
        BURGER_BUTTON = '//ytd-masthead//yt-icon[@id="guide-icon"]'
        VIDEO_HISTORY_BUTTON = '//ytd-guide-entry-renderer//a[@title="History"]'
        LIKED_VIDEOS_BUTTON = '//ytd-guide-entry-renderer//a[@title="Liked videos"]'
        AVATAR_BUTTON = '//button[@id="avatar-btn"]'
        CHANGE_LANGUAGE_BUTTON = '//div[@id="primary-text-container"]//yt-formatted-string[contains(text(), "Language:")]'
        # CHOOSE_YOUR_LANGUAGE = '//yt-formatted-string[text()="Choose your language"]'
        CHOOSE_ARABIC_LANGUAGE_ = '//yt-formatted-string[text()="العربية"]'
        SHORTS_BUTTON = '//ytd-guide-section-renderer//a[@title="Shorts"]'
    except c.NoSuchElementException as e:
        print("NoSuchElementException", e)

    def __init__(self, driver):
        super().__init__(driver)
        self._search_input = self._driver.find_element(By.XPATH, self.SEARCH_INPUT)
        self._search_icon = self._driver.find_element(By.XPATH, self.SEARCH_ICON)
        self._burger_button = self._driver.find_element(By.XPATH, self.BURGER_BUTTON)
        self._video_history_button = self._driver.find_element(By.XPATH, self.VIDEO_HISTORY_BUTTON)
        self._liked_video_button = self._driver.find_element(By.XPATH, self.LIKED_VIDEOS_BUTTON)
        self._avatr_profile_button = self._driver.find_element(By.XPATH, self.AVATAR_BUTTON)
        self._change_language_button = self._driver.find_element(By.XPATH, self.CHANGE_LANGUAGE_BUTTON)
        self._choose_arabic_language = self._driver.find_element(By.XPATH, self.CHOOSE_ARABIC_LANGUAGE_)
        self._shorts_button = self._driver.find_element(By.XPATH, self.SHORTS_BUTTON)
        
    def search_input(self, config):
        self._search_input.click()
        self._driver.send_keys(config)
        self._search_icon.click()
        
    def search_icon(self):
        self._search_input.click()
        
    def burger_button(self):
        self._burger_button.click()
        
    def video_history_button(self):
        self._burger_button()
        self._video_history_button.click()
        
    def liked_video_button(self):
        self._burger_button()
        self._liked_video_button.click()
        
    def avatr_profile_button(self):
        self._avatr_profile_button.click()
        
    def change_language_button(self):
        self._change_language_button.click()
        
    def choose_arabic_language(self):
        self._avatr_profile_button()
        self._change_language_button()
        self._choose_arabic_language.click()
        
    def shorts_button(self):
        self._shorts_button.click()
    
