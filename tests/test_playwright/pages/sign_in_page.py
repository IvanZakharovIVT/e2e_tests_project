from playwright.sync_api import Locator

from tests.test_playwright.pages.base_page import BasePage


class SignInPage(BasePage):
    """Страница авторизации"""
    INPUT_USERNAME_LOCATOR = "input[name='username']"
    INPUT_PASSWORD_LOCATOR = "input[name='password']"
    ERROR_MESSAGE_LOCATOR = ".B0FQjFgqnsXrRmLKgQG3"
    TITLE_LOCATOR = "div.VEk5WthgxYcIVhuIU03A > div > div.YhCboO0sYx3Lb7l8jhSG"
    SUBMIT_BUTTON = "button[type='submit']"

    @property
    def error_message_locator(self) -> Locator:
        return self.page.locator(self.ERROR_MESSAGE_LOCATOR)

    @property
    def title_locator(self) -> Locator:
        return self.page.locator(self.TITLE_LOCATOR)

    def insert_username(self, username: str):
        input_username = self.page.locator(self.INPUT_USERNAME_LOCATOR)
        input_username.fill(username)

    def insert_password(self, password: str):
        input_username = self.page.locator(self.INPUT_PASSWORD_LOCATOR)
        input_username.fill(password)

    def sign_in(self):
        self.page.locator(self.SUBMIT_BUTTON).click()
