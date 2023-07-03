from selene import browser, have,be

def test_cpmplete_todo():
    browser.open('/')
    browser.element('#new-todo').should(be.blank)

    browser.element('#new-todo').type('a').press_enter()
    browser.element('#new-todo').type('b').press_enter()
    browser.element('#new-todo').type('c').press_enter()
    browser.all('#todo-list>li').should(have.size(3))