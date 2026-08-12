from playwright.sync_api import Page, expect


def test_login_page_title(page: Page, request):
    request.node.test_id = "TC_001"
    request.node.scenario = "Verify Login Page Title"
    request.node.description = "Verify that the login page displays the correct title."
    request.node.steps = [
        "Open the login page",
        "Verify the page title"
    ]
    request.node.expected = "The Internet"

    page.goto("https://the-internet.herokuapp.com/login")

    actual = page.title()
    request.node.actual = actual

    expect(page).to_have_title(request.node.expected)


def test_login_page_url(page: Page, request):
    request.node.test_id = "TC_002"
    request.node.scenario = "Verify Login Page URL"
    request.node.description = "Verify that the login page URL is correct."
    request.node.steps = [
        "Open the login page",
        "Verify the current URL"
    ]
    request.node.expected = "https://the-internet.herokuapp.com/login"

    page.goto(request.node.expected)

    actual = page.url
    request.node.actual = actual

    expect(page).to_have_url(request.node.expected)