from conftest import page

class TestWikipedia:
    def test_find_python(self, page):
        """Поиск слова Python на странице Гвидо Ван Россума"""
        page.goto("https://www.wikipedia.org")
        input_field = page.locator('input[id="searchInput"]')
        input_field.fill("Гвидо Ван Россум")
        input_field.press("Enter")

        assert "Python" in page.inner_text("body")
