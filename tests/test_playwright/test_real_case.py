from conftest import page
from settings import TRACKER_USERNAME, TRACKER_PASSWORD, TRACKER_URL
from tests.test_playwright.pages.my_projects_page import MyProjectsPage
from tests.test_playwright.pages.sign_in_page import SignInPage


class TestRealCase:
    PROJECT_HREF = "/projects"

    def test_real_case(self, page):
        page.goto(TRACKER_URL)

        sign_in_page = SignInPage(page)
        my_project_page = MyProjectsPage(page)

        sign_in_page.insert_username(TRACKER_USERNAME)
        sign_in_page.insert_password(TRACKER_PASSWORD)
        sign_in_page.sign_in()

        current_page_selector = my_project_page.current_page_selector
        assert current_page_selector.get_attribute('href') == "/projects"

        my_project_page.select_project_type(1)

        my_project_page.insert_select_text("Привет")
