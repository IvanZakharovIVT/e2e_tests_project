import time

from fixtures.page import page
from settings import TRACKER_USERNAME, TRACKER_PASSWORD


class TestTracker:
    comment_text = "Разработка первых автотестов для работы с playwright"

    def test_set_and_remove_time(self, page):
        page.goto("http://track.nordclan/timereports")
        input_username = page.locator('input[name="username"]')
        input_username.fill(TRACKER_USERNAME)
        input_password = page.locator('input[name="password"]')
        input_password.fill(TRACKER_PASSWORD)
        input_password.press("Enter")

        time_report_button = page.locator('a[href="/timereports"]')

        time_report_button.click()

        add_activity = page.locator('.addActivity')
        add_activity.click()

        search_field = page.locator('.L40Ce1dkZzDwkTX8jmo3')
        search_field.click()
        search_field.fill("Подготовка")
        search_field.press("Enter")

        activity_button = page.locator('th:has-text("Подготовка к интервью")')
        activity_button.click()

        add_button = page.locator('button[type="submit"]')
        add_button.click()

        toggles = page.locator('.toggleComment')
        toggle_count = len(toggles.all())

        first_untrack_day = page.locator('input[value="0"]').first
        first_untrack_day.click()
        first_untrack_day.fill("8")

        comment = page.locator(f'tr.taskRow > td:nth-child({toggle_count + 2}) > div > div > .toggleComment')
        comment.click(timeout=5000)

        comment_input = page.locator('textarea')
        comment_input.fill(self.comment_text, timeout=5000)
        assert comment_input.input_value(timeout=5000) == self.comment_text

        confirm_button = page.locator('.XRVp4xxKofwvTTn6y8Y2')
        confirm_button.click()


        date_to_check = page.locator(
            f'.GSJEaIhqhOj5a1bwaWXu > th:nth-child({toggle_count + 2}) > div'
        ).text_content()[2:]
        time.sleep(2)

        total_toggle_comment = page.locator('.totalToggleComment')
        total_toggle_comment.click()

        toggle_list_locator = page.locator('.rGOECBNcTT2M4YU4zlJX')
        last_element = toggle_list_locator.locator('.SBRJyKo57H5f0mT3YNNL').last

        textarea = last_element.locator('textarea')
        textarea.wait_for(timeout=2000, state="attached")

        result_value = textarea.input_value()
        assert result_value == self.comment_text

        time_value = last_element.locator('.FHz42jZNAtn160bzlTQK').text_content()
        assert time_value.split(' ')[1] == date_to_check

