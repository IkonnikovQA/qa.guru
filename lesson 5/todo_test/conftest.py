import pytest
from selene import browser
from selenium import webdriver

@pytest.fixture(scope='function', autouse=True)
def browser_managment():
    browser.config.base_url = 'https://todomvc.com/examples/emberjs/'
    driver_options = webdriver.ChromeOptions()
    driver_options.add_argument('--headless')
    browser.config.driver_options = driver_options
    yield

    browser.quit()
