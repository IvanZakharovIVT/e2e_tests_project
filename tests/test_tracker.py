import re
from playwright.sync_api import Page, expect, sync_playwright

from fixtures.page import page

class TestFirst:
    def test_using_fixture(self, page):
        page.goto("google.com")
        print("123")
