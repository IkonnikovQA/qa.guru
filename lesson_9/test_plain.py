from selene import browser, have, by


def test_issue_name_for_github_repo_plain_selene():
    browser.open('https://github.com/')
    browser.element('.search-input-container').click()
    browser.element('#query-builder-test').type('eroshenkoam/allure-example').press_enter()
    browser.element(by.link_text('eroshenkoam/allure-example')).click()
    browser.element('#issues-tab').click()
    browser.element('#js-issues-search').type('allure').press_enter()
    assert browser.element('#issue_81_link').should(have.exact_text('issue_to_test_allure_report'))


def test_gihhub_pages():
    pass