from selene import browser, have, by
import allure
from allure_commons.types import Severity


@allure.tag('web')
@allure.severity(Severity.BLOCKER)
@allure.label('owner', 'nsbelova')
@allure.feature('Issues names')
@allure.story('Issues in public repository can be found')
@allure.link('https://github.com', name='Testing')
def test_issue_name_for_github_repo_dynamic_steps():
    with allure.step('Open main page'):
        browser.open('https://github.com/')

    with allure.step('Search for repository'):
        browser.element('.search-input-container').click()
        browser.element('#query-builder-test').type('eroshenkoam/allure-example').press_enter()

    with allure.step('Click on found repository'):
        browser.element(by.link_text('eroshenkoam/allure-example')).click()

    with allure.step('Switch to Issues tab'):
        browser.element('#issues-tab').click()

    with allure.step('Search for issue made for testing'):
        browser.element('#js-issues-search').type('allure').press_enter()

    with allure.step('Verify issue text'):
        assert browser.element('#issue_81_link').should(have.exact_text('issue_to_test_allure_report'))