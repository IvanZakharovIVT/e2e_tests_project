from fixtures.page import page
from settings import TRACKER_USERNAME, TRACKER_PASSWORD
from tests.test_playwright.pages.my_projects_page import MyProjectsPage
from tests.test_playwright.pages.sign_in_page import SignInPage


class TestTrackerProjectPages:
    comment_text = "Разработка первых автотестов для работы с playwright (page object_model)"
    TRACKER_URL = "http://track.nordclan/timereports"
    TASK_NAME = "Подготовка к интервью"

    def test_set_time(self, page):
        page.goto(self.TRACKER_URL)

        sign_in_page = SignInPage(page)
        my_project_page = MyProjectsPage(page)

        sign_in_page.insert_username(TRACKER_USERNAME)
        sign_in_page.insert_password(TRACKER_PASSWORD)
        sign_in_page.sign_in()

        current_href = my_project_page.get_current_page_selector_href()
        assert current_href == "/projects"

        my_project_page.insert_select_tag_text('NordClan')

        my_project_page.select_tag("backend")

        len_val = len(page.locator('.PpF9g_aq6_bfN5WC8Fkx > div.row').all())

        assert len_val == 1

        my_project_page.click_on_project_by_number(1)

