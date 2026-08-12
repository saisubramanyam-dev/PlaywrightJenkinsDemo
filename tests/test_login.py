from playwright.sync_api import Page, expect


def test_login_page_title(page: Page):
    page.goto("https://the-internet.herokuapp.com/login")

    expect(page).to_have_title("The Internet")


def test_login_page_url(page: Page):
    page.goto("https://the-internet.herokuapp.com/login")

    expect(page).to_have_url(
        "https://the-internet.herokuapp.com/login"
    )