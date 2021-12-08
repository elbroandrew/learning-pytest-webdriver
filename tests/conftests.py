import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as chrome_options


@pytest.fixture
def get_chrome_options():
    options = chrome_options()
    options.add_argument('chrome')  # Use headless if you don't need a browser UI.
    options.add_argument('--start-maximized')
    options.add_argument('--window-size=800,600')
    return options


@pytest.fixture
def get_webdriver():
    options = get_chrome_options()
    driver = webdriver.Chrome(
        executable_path='C:\Users\Andrew\PycharmProjects\pytest-venv\pytest_youtube\chromedriver',
        options=options
    )
    return driver

@pytest.fixture
def setup(request, get_webdriver):
    driver = get_webdriver()
    url = 'https://www.macys.com'
    if request.cls is not None:
        request.cls.driver = driver
    driver.get(url)
    yield driver
    driver.quit()


