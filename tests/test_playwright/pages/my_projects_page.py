from tests.test_playwright.pages.base_page import BasePage


class MyProjectsPage(BasePage):
    TIME_REPORT_BUTTON_LOCATOR = 'a[href="/timereports"]'

    def link_to_time_reports(self):
        time_report_button = self.page.locator(self.TIME_REPORT_BUTTON_LOCATOR)
        time_report_button.click()

    def get_current_page_selector_href(self) -> str:
        return self.page.locator('li > a.whSN_60dtoulJ6d2dCnt').get_attribute('href')

    def select_tag(self, tag_name: str):
        select_locator = self.page.locator('div[id="react-select-5--value"]')
        select_locator.click()
        self.page.locator(f'div[aria-label="{tag_name}"]').click()
        assert "backend" in self.page.locator('div[id="react-select-5--value"]').text_content()

    def insert_select_tag_text(self, select_text: str):
        search_input = self.page.locator('.L40Ce1dkZzDwkTX8jmo3')
        search_input.fill(select_text)
        search_input.press("Enter")

    def click_on_project_by_number(self, number: int):
        self.page.locator(f"div.row:nth-child({number}) > div > h3 > div > a").click()