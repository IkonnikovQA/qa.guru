import pytest
from selene import browser
import os


@pytest.fixture(scope='function', autouse=True)
def browser_management():
    browser.config.window_width = os.getenv('selene_window_width', 1920)
    browser.config.window_height = os.getenv('selene_window_height', 1080)
