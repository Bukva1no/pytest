from playwright.sync_api import Page, expect
import pytest
def login(page, username, password):
    page.goto("/")
    page.fill("#user-name", username)
    page.fill("#password", password)
    page.click("#login-button")



@pytest.fixture
def logged_in_page(page: Page):
    login(page, "standard_user", "secret_sauce")
    return page

class LoginPage:
    def __init__(self, page):
        self.page = page

    def login(self, username, password):
        self.page.goto("/")
        self.page.fill("#user-name", username)
        self.page.fill("#password", password)
        self.page.click("#login-button")

class InventoryPage:
    def __init__(self, page):
        self.page = page

    def get_product_count(self):
        return self.page.locator(".inventory_item").count()