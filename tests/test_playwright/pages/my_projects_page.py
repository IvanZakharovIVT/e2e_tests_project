from tests.test_playwright.pages.base_page import BasePage


class MyProjectsPage(BasePage):
    TIME_REPORT_BUTTON_LOCATOR = 'a[href="/timereports"]'

    def link_to_time_reports(self):
        time_report_button = self.page.locator(self.TIME_REPORT_BUTTON_LOCATOR)
        time_report_button.click()
