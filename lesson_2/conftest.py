import pytest


@pytest.fixture(scope="session", autouse=True)
def browser():
    print("Браузер стартует!")

    yield

    print("Браузер закрывается")