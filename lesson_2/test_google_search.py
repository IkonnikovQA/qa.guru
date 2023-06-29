import pytest
from selene.support.shared import browser
from selene import be, have


@pytest.fixture(scope="module")
def maximize_browser_window():
    browser.config.window_width = 1920
    browser.config.window_height = 1080


def test_google_search(maximize_browser_window):
    browser.open('https://google.com')
    browser.element('[name="q"]').should(be.blank).type('qa.guru').press_enter()
    browser.element('[id="search"]').should(have.text('QA.GURU — Курсы тестировщиков - онлайн-обучение ...'))
    print('Результаты поиска по строке содержат ожидаемый заголовок')


def test_no_search_results(maximize_browser_window):
    browser.open('https://google.com')
    random_string = 'E81RvIDd2KZrdsYQrwDRLsgbzVUOQy8naI9arDgwiijXiy1iX6'
    browser.element('[name="q"]').should(be.blank).type(random_string).press_enter()
    browser.element('[id="topstuff"]').should(have.text(f'По запросу {random_string} ничего не найдено.'))
    print('При поиске по произвольной строке ничего не находится')