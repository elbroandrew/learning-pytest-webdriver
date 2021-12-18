import time

import pytest
from pom.homepage_nav import HomepageNav


@pytest.mark.usefixtures('setup')
class TestHomepage:

    def test_nav_links(self):
        homepage_nav = HomepageNav(self.driver)
        homepage_nav.get_modal_window_close_button().click()
        homepage_nav.driver.delete_cookie('ak_bmsc')
        for idx in range(8):
            homepage_nav.get_nav_links()[idx].click()
            homepage_nav.driver.delete_cookie('ak_bmsc')


