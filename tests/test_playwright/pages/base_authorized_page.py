from tests.test_playwright.pages.base_page import BasePage


class BaseAuthorizedPage(BasePage):
    LOGOUT_LOCATOR = ".k2gytlkNhhzNzQuorSvq > .hf1tYUEEA_NTfJSWnRJA"

    def logout(self):
        logout_icon = self.page.locator(self.LOGOUT_LOCATOR)
        logout_icon.click()

    def link_to_page_from_sidebar(self, sidebar_href: str):
        time_report_button = self.page.locator(f".DrbfUacevysuNgEQlYpu > a[href='{sidebar_href}']")
        time_report_button.click()