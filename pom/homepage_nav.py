from base.seleniumbase import SeleniumBase
from selenium.webdriver.remote.webelement import WebElement


class HomepageNav(SeleniumBase):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.__nav_links: str = '#mainNavigationFobs>li'

    def get_nav_links(self) -> WebElement:
        return self.are_visible('css', self.__nav_links, 'Header Navigation Links')

