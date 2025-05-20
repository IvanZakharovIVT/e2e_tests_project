from playwright.sync_api import Locator

from tests.test_playwright.pages.base_page import BasePage


class MyProjectsPage(BasePage):
    """Страница 'Мои проекты'"""
    TIME_REPORT_BUTTON_LOCATOR = 'a[href="/timereports"]'
    ACTIVE_PAGE_BUTTON = 'li > a.whSN_60dtoulJ6d2dCnt'
    TAG_SELECTOR_LOCATOR = 'div[id="react-select-5--value"]'
    PROJECT_TYPE_SELECT_LOCATOR = 'div[id="react-select-4--value"]'
    SEARCH_FIELD_LOCATOR = '.L40Ce1dkZzDwkTX8jmo3'

    @property
    def current_page_locator(self) -> Locator:
        return self.page.locator(self.ACTIVE_PAGE_BUTTON)

    @property
    def project_type_locator(self) -> Locator:
        return self.page.locator(self.PROJECT_TYPE_SELECT_LOCATOR)

    @property
    def search_input_locator(self) -> Locator:
        return self.page.locator(self.SEARCH_FIELD_LOCATOR)

    def link_to_time_reports(self):
        time_report_button = self.page.locator(self.TIME_REPORT_BUTTON_LOCATOR)
        time_report_button.click()

    def select_tag(self, tag_name: str):
        """Выбор тега"""
        select_locator = self.page.locator(self.TAG_SELECTOR_LOCATOR)
        select_locator.click()
        self.page.locator(f'div[aria-label="{tag_name}"]').click()
        assert tag_name in select_locator.text_content()

    def select_project_type(self, project_type: int):
        """Выбор типа проекта"""
        self.project_type_locator.click()
        self.page.locator(f'div[id="react-select-4--option-{project_type}"]').click()

    def insert_select_text(self, select_text: str):
        """Ввод текста для поиска"""
        self.search_input_locator.fill(select_text)
        self.search_input_locator.press("Enter")

    def click_on_project_by_number(self, number: int):
        """Выбор проекта по его номеру в таблице"""
        self.page.locator(f"div.row:nth-child({number}) > div > h3 > div > a").click()