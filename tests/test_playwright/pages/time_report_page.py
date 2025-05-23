from playwright.sync_api import expect, Locator

from tests.test_playwright.pages.base_authorized_page import BaseAuthorizedPage


class TimeReportPage(BaseAuthorizedPage):
    """Страница отчетов по времени"""
    ADD_ACTIVITY_BUTTON_LOCATOR = ".addActivity"
    COMMENT_TEXTAREA_LOCATOR = "div.SUt_25F2Dvm9m866G6fm  > textarea"
    CONFIRM_BUTTON_LOCATOR = ".XRVp4xxKofwvTTn6y8Y2"
    TOGGLE_LIST_ICON_LOCATOR = ".rGOECBNcTT2M4YU4zlJX"
    ACTIVITY_REPORTS_LOCATOR = ".SBRJyKo57H5f0mT3YNNL"
    ROW_LABELS_LOCATOR = "tr.taskRow > td:nth-child(1) >div >div > a"

    @property
    def activity_reports(self) -> Locator:
        toggle_list_locator = self.page.locator(self.TOGGLE_LIST_ICON_LOCATOR)
        return toggle_list_locator.locator(self.ACTIVITY_REPORTS_LOCATOR)

    @property
    def row_labels(self) -> list[Locator]:
        return self.page.locator(self.ROW_LABELS_LOCATOR).all()

    def get_date_value_by_column(self, column_number: int) -> str:
        return self.page.locator(
            f".GSJEaIhqhOj5a1bwaWXu > th:nth-child({column_number}) > div"
        ).text_content()[2:]

    def get_active_toggles_in_row(self, row_number: int) -> list[Locator]:
        return self.page.locator(f"tr.taskRow:nth-child({row_number}) > td > div > div > .toggleComment").all()

    def add_activity(self):
        """Добавление новой задачи"""
        add_activity = self.page.locator(self.ADD_ACTIVITY_BUTTON_LOCATOR)
        add_activity.click()

    def add_new_day_time(self, column_number: int, row_number: int, time_value: int):
        """Добавление времени в ячейку по столбцу и строке"""
        first_untrack_day = self.page.locator(
            f"tr.taskRow:nth-child({row_number}) > td:nth-child({column_number}) > div > div > input[value='0']"
        )
        first_untrack_day.click()
        first_untrack_day.fill(str(time_value))

    def click_to_comment_icon(self, column_number: int, row_number: int):
        comment = self.page.locator(
            f"tr.taskRow:nth-child({row_number}) > td:nth-child({column_number}) > div > div > .toggleComment"
        )
        comment.click(timeout=5000)

    def add_comment(self, comment_text:str):
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
