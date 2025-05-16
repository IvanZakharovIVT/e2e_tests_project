import time
from datetime import datetime

from fixtures.page import page
from settings import TRACKER_USERNAME, TRACKER_PASSWORD


class TestTracker:
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

        first_untrack_day = page.locator('input[value="0"]').first
        first_untrack_day.click()
        first_untrack_day.fill("8")

        time.sleep(5)

        comment = page.locator('.toggleComment').last
        comment.click()

        comment_input = page.locator('textarea')
        comment_input.fill("Комментарий")

        confirm_button = page.locator('.XRVp4xxKofwvTTn6y8Y2')
        confirm_button.click()

        total_toggle_comment = page.locator('.totalToggleComment')
        total_toggle_comment.click()

        toggle_list_locator = page.locator('.rGOECBNcTT2M4YU4zlJX')
        last_element = toggle_list_locator.locator('.SBRJyKo57H5f0mT3YNNL').last

        result_value = last_element.locator('textarea').last.input_value()
        assert result_value == "Комментарий"

        time_value = last_element.locator('.FHz42jZNAtn160bzlTQK').text_content(timeout=10)
        assert time_value.split(' ')[1] == datetime.today().date().strftime('%d.%m')

