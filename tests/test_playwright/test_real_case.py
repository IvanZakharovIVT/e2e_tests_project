from conftest import page
from settings import TRACKER_USERNAME, TRACKER_PASSWORD, TRACKER_URL
from tests.test_playwright.pages.my_projects_page import MyProjectsPage
from tests.test_playwright.pages.sign_in_page import SignInPage


class TestRealCase:
    """Основной тест по кейсу"""
    PROJECT_HREF = "/projects"
    SEARCH_INPUT_VALUE = "Привет"

    def test_real_case(self, page):
        page.goto(TRACKER_URL)

        sign_in_page = SignInPage(page)
        my_project_page = MyProjectsPage(page)

        sign_in_page.insert_username(TRACKER_USERNAME)
        sign_in_page.insert_password(TRACKER_PASSWORD)
        sign_in_page.sign_in()

        current_page_selector = my_project_page.current_page_locator
        assert current_page_selector.get_attribute('href') == self.PROJECT_HREF

        my_project_page.select_project_type(1)
        assert my_project_page.project_type_locator.text_content().strip() == "×Internal"

        my_project_page.insert_select_text(self.SEARCH_INPUT_VALUE)
        assert my_project_page.search_input_locator.input_value() == self.SEARCH_INPUT_VALUE

    def test_auth_error(self, page):
        page.goto(TRACKER_URL)

        sign_in_page = SignInPage(page)

        sign_in_page.insert_username("wrong_username")
        sign_in_page.insert_password("wrong_password")
        sign_in_page.sign_in()

        error_message_locator = page.locator(".B0FQjFgqnsXrRmLKgQG3")

        assert error_message_locator.text_content().strip() == "Неверный логин/пароль. Проверьте данные"
