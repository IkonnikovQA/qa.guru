import allure
from selene import by
from selene.support.conditions import be
from selene.support.shared import browser
from selene.support.shared.jquery_style import s


number = '#81'
repo = 'eroshenkoam/allure-example'
def test_dynamic_step():
    with allure.step('Открываем главную страницу'):
        browser.open('https://github.com/')

    with allure.step('Кликаем поиск'):
        s('.search-input-container').click()

    with allure.step('Вводим в поиск'):
        s('#query-builder-test').send_keys(repo).press_enter()

    with allure.step('Открываем репозиторий'):
        s(by.link_text(repo)).click()

    with allure.step('Кликаем по ишью'):
        s('#issues-tab').click()

    with allure.step('Отчет'):
        s(by.partial_text('#81')).should(be.visible)


def test_decorator_steps():
    open_main_page()
    search_for_repository('eroshenkoam/allure-example')
    go_to_repository("eroshenkoam/allure-example")
    go_to_issue()
    should_text_issue('#81')
@allure.step('Открываем главную страницу')
def open_main_page():
    browser.open('https://github.com/')

@allure.step('Ищем репозиторий {repo}')
def search_for_repository(repo):
    s('.search-input-container').click()
    s('#query-builder-test').send_keys(repo).press_enter()

@allure.step('Переходим в {repo}')
def go_to_repository(repo):
    s(by.link_text(repo)).click()

@allure.step('Кликаем по ишью')
def go_to_issue():
    s('#issues-tab').click()

@allure.step('Проверяем наличие Issue с номером {number}')
def should_text_issue(number):
    s(by.partial_text(number)).should(be.visible)
