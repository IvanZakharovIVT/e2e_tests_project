from playwright.sync_api import Page, expect

from tests.test_pages.pages.base_page import BasePage


class TimeReportPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.toggle_count = 0
        self.date_to_check = ""

    def add_activity(self):
        add_activity = self.page.locator('.addActivity')
        add_activity.click()

        search_field = self.page.locator('.L40Ce1dkZzDwkTX8jmo3')
        search_field.click()
        search_field.fill("Подготовка")
        search_field.press("Enter")

        activity_button = self.page.locator('th:has-text("Подготовка к интервью")')
        activity_button.click()

        add_button = self.page.locator('button[type="submit"]')
        add_button.click()

        toggles = self.page.locator('.toggleComment')
        self.toggle_count = len(toggles.all())
        self.date_to_check = self.page.locator(
            f'.GSJEaIhqhOj5a1bwaWXu > th:nth-child({self.toggle_count + 2}) > div'
        ).text_content()[2:]

    def add_new_day_time(self):
        first_untrack_day = self.page.locator('input[value="0"]').first
        first_untrack_day.click()
        first_untrack_day.fill("8")

    def add_comment_to_last_day(self, comment_text:str):
        comment = self.page.locator(f'tr.taskRow > td:nth-child({self.toggle_count + 2}) > div > div > .toggleComment')
        comment.click(timeout=5000)

        comment_input = self.page.locator('div.SUt_25F2Dvm9m866G6fm  > textarea')
        comment_input.fill(comment_text, timeout=5000)
        expect(comment_input).to_have_value(comment_text, timeout=5000)

        confirm_button = self.page.locator('.XRVp4xxKofwvTTn6y8Y2')
        confirm_button.click()


    def get_last_report_item(self):
        total_toggle_comment = self.page.locator('.totalToggleComment')
        total_toggle_comment.click()

        toggle_list_locator =self. page.locator('.rGOECBNcTT2M4YU4zlJX')
        last_element = toggle_list_locator.locator('.SBRJyKo57H5f0mT3YNNL').last
        return last_element