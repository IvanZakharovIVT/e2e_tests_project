from tests.test_pages.pages.base_page import BasePage


class AddNewActivityWindow(BasePage):
    def find_activity(self):
        search_field = self.page.locator('.L40Ce1dkZzDwkTX8jmo3')
        search_field.click()
        search_field.fill("Подготовка")
        search_field.press("Enter")

    def add_activity(self):
        activity_button = self.page.locator('th:has-text("Подготовка к интервью")')
        activity_button.click()

        add_button = self.page.locator('button[type="submit"]')
        add_button.click()