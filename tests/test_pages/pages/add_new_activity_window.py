from tests.test_pages.pages.base_page import BasePage


class AddNewActivityWindow(BasePage):
    def find_activity(self, activity_task: str):
        search_field = self.page.locator('.L40Ce1dkZzDwkTX8jmo3')
        search_field.click()
        search_field.fill(activity_task)
        search_field.press("Enter")

    def add_activity(self, activity_task: str):
        activity_button = self.page.locator(f'th:has-text("{activity_task}")')
        activity_button.click()

        add_button = self.page.locator('button[type="submit"]')
        add_button.click()