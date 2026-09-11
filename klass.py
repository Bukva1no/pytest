from playwright.sync_api import Page, expect
from conftest import login, LoginPage

import pytest


def test_login_via_page_object(page: Page):
    login_page = LoginPage(page)
    login_page.login("standard_user", "secret_sauce")
    expect(page).to_have_url("https://www.saucedemo.com/inventory.html")