from selene import browser, have, by
import allure
from allure_commons.types import Severity


@allure.tag('web')
@allure.severity(Severity.CRITICAL)
@allure.label('owner', 'nbelova')
@allure.feature('Issues in public repository')
@allure.story('Data in public repository is visible for users')
@allure.link('https://github.com', name='Testing')
def test_issue_name_for_github_repo_static_steps():
    open_main_page()
    search_for_repository('eroshenkoam/allure-example')
    follow_repo_link('eroshenkoam/allure-example')
    go_to_issues_tab()
    search_for_issue_containing_text('allure')
    verify_title('issue_to_test_allure_report')


@allure.step('Open main page')
def open_main_page():
    browser.open('https://github.com/')


@allure.step('Search for repository {repo}')
def search_for_repository(repo):
    browser.element('.search-input-container').click()
    browser.element('#query-builder-test').type(repo).press_enter()


@allure.step('Click on found repository {repo}')
def follow_repo_link(repo):
    browser.element(by.link_text(repo)).click()


@allure.step('Switch to Issues tab')
def go_to_issues_tab():
    browser.element('#issues-tab').click()


@allure.step('Search for issue made for testing using text {issue_search_text}')
def search_for_issue_containing_text(issue_search_text):
    browser.element('#js-issues-search').type(issue_search_text).press_enter()


@allure.step('Verify issue text is {issue_title}')
def verify_title(issue_title):
    assert browser.element('#issue_81_link').should(have.exact_text(issue_title))