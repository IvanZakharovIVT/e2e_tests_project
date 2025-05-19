from fixtures.page import page
from settings import TRACKER_USERNAME, TRACKER_PASSWORD
from tests.test_playwright.pages.my_projects_page import MyProjectsPage
from tests.test_playwright.pages.sign_in_page import SignInPage


class TestRealCase:
    TRACKER_URL = "http://track.nordclan/timereports"

    def test_real_case(self, page):
        page.goto(self.TRACKER_URL)

        sign_in_page = SignInPage(page)
        my_project_page = MyProjectsPage(page)

        sign_in_page.insert_username(TRACKER_USERNAME)
        sign_in_page.insert_password(TRACKER_PASSWORD)
        sign_in_page.sign_in()

        current_href = my_project_page.get_current_page_selector_href()
        assert current_href == "/projects"

        my_project_page.select_project_type(1)

