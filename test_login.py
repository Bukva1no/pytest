from playwright.sync_api import Page, expect

def test_successful_login(page: Page):
    page.goto("https://the-internet.herokuapp.com/login")

    page.fill("#username", "tomsmith")
    page.fill("#password", "SuperSecretPassword!")
    page.click("button[type='submit']")

    expect(page).to_have_url("https://the-internet.herokuapp.com/secure")

