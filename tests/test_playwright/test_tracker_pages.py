from playwright.sync_api import expect

from conftest import page
from settings import TRACKER_USERNAME, TRACKER_PASSWORD, TRACKER_URL
from tests.test_playwright.pages.add_new_activity_window import AddNewActivityWindow
from tests.test_playwright.pages.my_projects_page import MyProjectsPage
from tests.test_playwright.pages.sign_in_page import SignInPage
from tests.test_playwright.pages.time_report_page import TimeReportPage


class TestTrackerPages:
    """Тест добавления новой записи в трекер с использованием page object_model"""
    COMMENT_TEXT = "Разработка первых автотестов для работы с playwright (page object_model)"
    TASK_NAME = "Подготовка к интервью"
    ROW_LABEL_LOCATOR = "tr.taskRow > td:nth-child(1) >div >div > a"

    def test_set_time(self, page):
        page.goto(TRACKER_URL)

        # Инициализация страниц
        sign_in_page = SignInPage(page)
        my_project_page = MyProjectsPage(page)
        time_report_page = TimeReportPage(page)
        add_activity_window = AddNewActivityWindow(page)

        # Авторизация
        sign_in_page.insert_username(TRACKER_USERNAME)
        sign_in_page.insert_password(TRACKER_PASSWORD)
        sign_in_page.sign_in()

        # Переход на страницу отчетов по времени
        my_project_page.link_to_time_reports()

        # Открытие диалогового окна добавления новой записи
        time_report_page.add_activity()

        # Добавление новой записи
        add_activity_window.find_activity(self.TASK_NAME)
        add_activity_window.add_activity(self.TASK_NAME)

        # Поиск номера строки добавленной задачи
        row_number = None
        for index, locator in enumerate(page.locator(self.ROW_LABEL_LOCATOR).all(), 1):
            if self.TASK_NAME in locator.text_content():
                row_number = index
                break
        assert row_number is not None

        # Получение позиции и даты, в которую необходимо записать время
        toggles = page.locator(f"tr.taskRow:nth-child({row_number}) > td > div > div > .toggleComment")
        toggle_count = len(toggles.all())
        date_to_check = page.locator(
            f".GSJEaIhqhOj5a1bwaWXu > th:nth-child({toggle_count + 2}) > div"
        ).text_content()[2:]

        # Добавление времени и комментария по строке и столбцу
        time_report_page.add_new_day_time(toggle_count, row_number, 8)
        time_report_page.add_comment_to_last_day(self.COMMENT_TEXT, toggle_count, row_number)
        time_report_page.confirm_comment()

        # Получение последнего элемента в списке отчету по всем дням
        time_report_page.click_to_all_activity_icon(row_number)
        last_element = time_report_page.activity_reports.last

        textarea = last_element.locator("textarea")

        expect(textarea).to_have_value(self.COMMENT_TEXT, timeout=5000)

        time_value = last_element.locator(".FHz42jZNAtn160bzlTQK").text_content()
        assert time_value.split(" ")[1] == date_to_check
