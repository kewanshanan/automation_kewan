from selenium.webdriver.common.by import By
from intro_to_selenium.youtube_task.infra.basepage import BasePage


class HomePage(BasePage):
    YOUTUBE_LOGO = '//ytd-masthead//a[@class="yt-simple-endpoint style-scope ytd-topbar-logo-renderer"]'
    SEARCH_INPUT = '//input[@id="search"]'
    BURGER_BUTTON = '//ytd-masthead//yt-icon[@id="guide-icon"]'
    VIDEO_HISTORY_BUTTON = '//ytd-masthead//div[@id="video-history"]'
    LIKED_VIDEOS_BUTTON = '//ytd-masthead//div[@id="video-list"]'

    def __init__(self, driver):
        super().__init__(driver)
