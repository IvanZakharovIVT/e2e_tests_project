from playwright.sync_api import expect

from fixtures.page import page
from settings import TRACKER_USERNAME, TRACKER_PASSWORD
from tests.test_pages.pages.add_new_activity_window import AddNewActivityWindow
from tests.test_pages.pages.my_projects_page import MyProjectsPage
from tests.test_pages.pages.sign_in_page import SignInPage
from tests.test_pages.pages.time_report_page import TimeReportPage


class TestTrackerPages:
    comment_text = "Разработка первых автотестов для работы с playwright (page object_model)"
    TRACKER_URL = "http://track.nordclan/timereports"

    def test_set_time(self, page):
        page.goto(self.TRACKER_URL)
        sign_in_page = SignInPage(page)
        my_project_page = MyProjectsPage(page)
        time_report_page = TimeReportPage(page)
        add_activity_window = AddNewActivityWindow(page)

        sign_in_page.insert_username(TRACKER_USERNAME)
        sign_in_page.insert_password(TRACKER_PASSWORD)
        sign_in_page.sign_in()

        my_project_page.link_to_time_reports()

        time_report_page.add_activity()

        add_activity_window.find_activity()

        add_activity_window.add_activity()

        toggles = page.locator('.toggleComment')
        toggle_count = len(toggles.all())
        date_to_check = page.locator(
            f'.GSJEaIhqhOj5a1bwaWXu > th:nth-child({toggle_count + 2}) > div'
        ).text_content()[2:]

        time_report_page.add_new_day_time()

        time_report_page.add_comment_to_last_day(self.comment_text, toggle_count)

        last_element = time_report_page.get_last_report_item()

        textarea = last_element.locator('textarea')

        expect(textarea).to_have_value(self.comment_text, timeout=5000)

        time_value = last_element.locator('.FHz42jZNAtn160bzlTQK').text_content()
        assert time_value.split(' ')[1] == date_to_check
