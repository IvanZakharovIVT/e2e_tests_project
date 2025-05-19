from tests.test_playwright.pages.base_page import BasePage


class SignInPage(BasePage):
    def insert_username(self, username: str):
        input_username = self.page.locator('input[name="username"]')
        input_username.fill(username)

    def insert_password(self, password: str):
        input_username = self.page.locator('input[name="password"]')
        input_username.fill(password)

    def sign_in(self):
        self.page.locator('button[type="submit"]').click()
