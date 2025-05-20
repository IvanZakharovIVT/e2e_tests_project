from fixtures.page import page

class TestFirst:
    def test_using_fixture(self, page):
        page.goto("https://www.wikipedia.org")
        input_field = page.locator('input[id="searchInput"]')
        input_field.fill("Гвидо Ван Россум")
        input_field.press("Enter")

        assert "Python" in page.inner_text("body")
