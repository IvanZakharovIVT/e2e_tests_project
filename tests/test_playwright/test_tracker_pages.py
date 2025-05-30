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
        my_project_page.link_to_page_from_sidebar("/timereports")

        # Открытие диалогового окна добавления новой записи
        time_report_page.add_activity()

        # Добавление новой записи
        add_activity_window.find_activity(self.TASK_NAME)
        add_activity_window.add_activity(self.TASK_NAME)

        # Поиск номера строки добавленной задачи
        row_number = None
        for index, locator in enumerate(time_report_page.row_labels, 1):
            if self.TASK_NAME in locator.text_content():
                row_number = index
                break
        assert row_number is not None

        # Получение позиции и даты, в которую необходимо записать время
        toggles = time_report_page.get_active_toggles_in_row(row_number)
        column_number = len(toggles) + 2
        date_to_check = time_report_page.get_date_value_by_column(column_number)

        # Добавление времени и комментария по строке и столбцу
        time_report_page.add_new_day_time(column_number, row_number, 8)
        time_report_page.click_to_comment_icon(column_number, row_number)
        time_report_page.add_comment(self.COMMENT_TEXT)
        time_report_page.confirm_comment()

        # Получение последнего элемента в списке отчету по всем дням
        time_report_page.click_to_all_activity_icon(row_number)
        last_element = time_report_page.activity_reports.last

        textarea = last_element.locator("textarea")

        expect(textarea).to_have_value(self.COMMENT_TEXT, timeout=5000)

        time_value = last_element.locator(".FHz42jZNAtn160bzlTQK").text_content()
        assert time_value.split(" ")[1] == date_to_check
