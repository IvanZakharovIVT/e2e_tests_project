from playwright.sync_api import expect, Page

from tests.test_pages.pages.base_page import BasePage


class TimeReportPage(BasePage):
    def add_activity(self):
        add_activity = self.page.locator('.addActivity')
        add_activity.click()

    def add_new_day_time(self):
        first_untrack_day = self.page.locator('input[value="0"]').first
        first_untrack_day.click()
        first_untrack_day.fill("8")

    def add_comment_to_last_day(self, comment_text:str, toggle_count: int, row_number: int):
        comment = self.page.locator(
            f'tr.taskRow:nth-child({row_number}) > td:nth-child({toggle_count + 2}) > div > div > .toggleComment'
        )
        comment.click(timeout=5000)

        comment_input = self.page.locator('div.SUt_25F2Dvm9m866G6fm  > textarea')
        comment_input.click()
        comment_input.fill(comment_text, timeout=5000)
        expect(comment_input).to_have_value(comment_text, timeout=5000)

        confirm_button = self.page.locator('.XRVp4xxKofwvTTn6y8Y2')
        confirm_button.click()

    def get_last_report_item(self, row_number: int):
        total_toggle_comment = self.page.locator(
            f'tr.taskRow:nth-child({row_number}) > td > div > .totalToggleComment'
        )
        total_toggle_comment.click()

        toggle_list_locator =self. page.locator('.rGOECBNcTT2M4YU4zlJX')
        last_element = toggle_list_locator.locator('.SBRJyKo57H5f0mT3YNNL').last
        return last_element
