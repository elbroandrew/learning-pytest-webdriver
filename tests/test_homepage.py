import time

import pytest
from pom.homepage_nav import HomepageNav


@pytest.mark.usefixtures('setup')
class TestHomepage:

    def test_nav_links(self):
        homepage_nav = HomepageNav(self.driver)
        homepage_nav.get_modal_window_close_button().click()
        cookies = homepage_nav.driver.get_cookies()
        cookies_names = [cookie['name'] for cookie in cookies]
        print(cookies)
        print('---------------------------------------')
        print(cookies_names)
        for idx in range(8):
            #homepage_nav.get_nav_links()[idx].click()
            for cookie_name in cookies_names:
                homepage_nav.driver.delete_cookie(cookie_name)
                homepage_nav.driver.refresh()
                homepage_nav.is_visible('tag_name', 'h1', cookie_name)
            time.sleep(1.5)


