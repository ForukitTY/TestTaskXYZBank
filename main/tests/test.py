import pytest

from main.pages.base_page import BasePage


def test(browser):
    page = BasePage(browser)
    page.open()
