import pytest
from playwright.sync_api import sync_playwright


@pytest.fixture(scope="module")
def page():
    with sync_playwright() as playwright:
        # Запускаем браузер (не в headless режиме)
        browser = playwright.chromium.launch(headless=False)

        # Создаем новую страницу
        page = browser.new_page()

        yield page

        browser.close()
