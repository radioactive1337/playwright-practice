import pytest
from playwright.sync_api import sync_playwright

DEFAULT_BROWSER = 'chromium'


def pytest_addoption(parser):
    parser.addoption("--headless", action="store_true", default=False)


@pytest.fixture(scope='session')
def page(request):
    browser_type = request.config.getoption('browser') or DEFAULT_BROWSER
    headless = request.config.getoption('headless')

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=headless) \
            if browser_type == 'chromium' else p.firefox.launch(headless=headless)
        context = browser.new_context()
        page = context.new_page()
        yield page
        page.close()
        context.close()
        browser.close()
