from playwright.sync_api import expect, Locator

from tests.test_playwright.pages.base_page import BasePage


class TimeReportPage(BasePage):
    """Страница отчетов по времени"""
    ADD_ACTIVITY_BUTTON_LOCATOR = ".addActivity"
    COMMENT_TEXTAREA_LOCATOR = "div.SUt_25F2Dvm9m866G6fm  > textarea"
    CONFIRM_BUTTON_LOCATOR = ".XRVp4xxKofwvTTn6y8Y2"

    @property
    def activity_reports(self) -> Locator:
        toggle_list_locator = self.page.locator(".rGOECBNcTT2M4YU4zlJX")
        return toggle_list_locator.locator(".SBRJyKo57H5f0mT3YNNL")

    def add_activity(self):
        """Добавление новой задачи"""
        add_activity = self.page.locator(self.ADD_ACTIVITY_BUTTON_LOCATOR)
        add_activity.click()

    def add_new_day_time(self, toggle_count: int, row_number: int, time_value: int):
        """Добавление времени в ячейку по столбцу и строке"""
        first_untrack_day = self.page.locator(
            f"tr.taskRow:nth-child({row_number}) > td:nth-child({toggle_count + 2}) > div > div > input[value='0']"
        )
        first_untrack_day.click()
        first_untrack_day.fill(str(time_value))

    def add_comment_to_last_day(self, comment_text:str, toggle_count: int, row_number: int):
        """Добавление комментария в ячейку по столбцу и строке"""
        comment = self.page.locator(
            f"tr.taskRow:nth-child({row_number}) > td:nth-child({toggle_count + 2}) > div > div > .toggleComment"
        )
        comment.click(timeout=5000)

        comment_input = self.page.locator(self.COMMENT_TEXTAREA_LOCATOR)
        comment_input.click()
        comment_input.fill(comment_text, timeout=5000)
        expect(comment_input).to_have_value(comment_text, timeout=5000)

    def confirm_comment(self):
        confirm_button = self.page.locator(self.CONFIRM_BUTTON_LOCATOR)
        confirm_button.click()

    def click_to_all_activity_icon(self, row_number: int):
        total_toggle_comment = self.page.locator(
            f"tr.taskRow:nth-child({row_number}) > td > div > .totalToggleComment"
        )
        total_toggle_comment.click()
