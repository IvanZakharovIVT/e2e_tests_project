from tests.test_playwright.pages.base_page import BasePage


class SignInPage(BasePage):
    """Страница авторизации"""
    INPUT_USERNAME_LOCATOR = 'input[name="username"]'
    INPUT_PASSWORD_LOCATOR = 'input[name="password"]'
    SUBMIT_BUTTON = 'button[type="submit"]'

    def insert_username(self, username: str):
        input_username = self.page.locator(self.INPUT_USERNAME_LOCATOR)
        input_username.fill(username)

    def insert_password(self, password: str):
        input_username = self.page.locator(self.INPUT_PASSWORD_LOCATOR)
        input_username.fill(password)

    def sign_in(self):
        self.page.locator(self.SUBMIT_BUTTON).click()
