from selenium.webdriver.support.events import AbstractEventListener


class MyListener(AbstractEventListener):
    def before_click(self, element, driver) -> None:
        driver.delete_cookie('ak_bmsc')

    def after_click(self, element, driver) -> None:
        driver.delete_cookie('ak_bmsc')