from selene import by
from selene.support.conditions import be
from selene.support.shared import browser
from selene.support.shared.jquery_style import s


def test_github():
    browser.open('https://github.com/')
    s('.search-input-container').click()
    s('#query-builder-test').send_keys('eroshenkoam/allure-example').press_enter()

    s(by.link_text('eroshenkoam/allure-example')).click()

    s('#issues-tab').click()

    s(by.partial_text('#81')).should(be.visible)

