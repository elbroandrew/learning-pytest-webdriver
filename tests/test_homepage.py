import time

import pytest
from pom.homepage_nav import HomepageNav


@pytest.mark.usefixtures('setup')
class TestHomepage:

    def test_nav_links(self):
        homepage_nav = HomepageNav(self.driver)
        homepage_nav.get_modal_window_close_button().click()
        actual_links = homepage_nav.get_nav_links_text()
        expected_links = homepage_nav.NAV_LINKS_TEXT
        assert expected_links == actual_links, 'Validating nav links'
        #homepage_nav.get_nav_link_by_name('Home').click()
        elements = homepage_nav.get_nav_links()
        for element in elements:
            element.click()
            time.sleep(2)


