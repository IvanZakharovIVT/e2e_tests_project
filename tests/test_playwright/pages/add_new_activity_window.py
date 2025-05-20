from tests.test_playwright.pages.base_page import BasePage


class AddNewActivityWindow(BasePage):
    SEARCH_FIELD_LOCATOR = '.L40Ce1dkZzDwkTX8jmo3'
    SUBMIT_BUTTON = 'button[type="submit"]'

    def find_activity(self, activity_task: str):
        search_field = self.page.locator(self.SEARCH_FIELD_LOCATOR)
        search_field.click()
        search_field.fill(activity_task)
        search_field.press("Enter")

    def add_activity(self, activity_task: str):
        activity_button = self.page.locator(f'th:has-text("{activity_task}")')
        activity_button.click()

        add_button = self.page.locator(self.SUBMIT_BUTTON)
        add_button.click()