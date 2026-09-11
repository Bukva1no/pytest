from playwright.sync_api import Page, expect

def login(page, username, password):
    page.goto("https://www.saucedemo.com")
    page.fill("#user-name", username)
    page.fill("#password", password)
    page.click("#login-button")

def test_successful_login(page: Page):
    login(page, "standard_user", "secret_sauce")
    expect(page).to_have_url("https://www.saucedemo.com/inventory.html")

def test_locked_out_user_shows_error(page: Page):
    login(page, "locked_out_user", "secret_sauce")
    error_message = page.get_by_text("Epic sadface: Sorry, this user has been locked out.")
    expect(error_message).to_be_visible()