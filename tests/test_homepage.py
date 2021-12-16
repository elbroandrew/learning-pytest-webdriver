import time

import pytest
from pom.homepage_nav import HomepageNav


@pytest.mark.usefixtures('setup')
class TestHomepage:

    def test_homepage(self):
        homepage_nav = HomepageNav(self.driver)
        actual_links = homepage_nav.get_nav_links_text()
        expected_links = homepage_nav.NAV_LINKS_TEXT
        assert expected_links == actual_links, 'Validating nav links'
        homepage_nav.get_nav_link_name('Home').click()
        time.sleep(5)


