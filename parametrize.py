from playwright.sync_api import Page, expect
from conftest import login

import pytest

@pytest.mark.parametrize("username, password, expected_url", [
    ("standard_user", "secret_sauce", "https://www.saucedemo.com/inventory.html"),
    ("problem_user", "secret_sauce", "https://www.saucedemo.com/inventory.html"),
])
def test_login_success(page: Page, username, password, expected_url):
    login(page, username, password)
    expect(page).to_have_url(expected_url)

def test_inventory_page_has_six_products(logged_in_page: Page):
    products = logged_in_page.locator(".inventory_item")
    expect(products).to_have_count(6)

def test_locked_out_user_shows_error(page: Page):
    login(page, "locked_out_user", "secret_sauce")
    error_message = page.get_by_text("Epic sadface: Sorry, this user has been locked out.")
    expect(error_message).to_be_visible()

def test_problem_user_same_image_bug(page: Page):
    login(page, "problem_user", "secret_sauce")

    images = page.locator(".inventory_item img")
    count = images.count()

    sources = []
    for i in range(count):
        src = images.nth(i).get_attribute("src")
        sources.append(src)

    unique_sources = set(sources)
    assert len(unique_sources) == 1