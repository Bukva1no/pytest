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

def test_problem_user(page: Page):
    login(page, "problem_user", "secret_sauce")
    expect(page).to_have_url("https://www.saucedemo.com/inventory.html")

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