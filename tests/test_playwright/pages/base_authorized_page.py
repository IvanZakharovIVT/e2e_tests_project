from tests.test_playwright.pages.base_page import BasePage


class BaseAuthorizedPage(BasePage):
    LOGOUT_LOCATOR = ".k2gytlkNhhzNzQuorSvq > .hf1tYUEEA_NTfJSWnRJA"

    def logout(self):
        logout_icon = self.page.locator(self.LOGOUT_LOCATOR)
        logout_icon.click()
