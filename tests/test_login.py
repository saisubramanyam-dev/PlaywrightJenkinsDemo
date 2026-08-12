from playwright.sync_api import Page, expect


def test_login_page_title(page: Page, request):
    test_id = "TC_001"
    scenario = "Verify Login Page Title"
    description = "Verify that the login page displays the correct title."
    steps = "1. Open login page\n2. Verify page title"
    expected = "The Internet"

    page.goto("https://the-internet.herokuapp.com/login")

    actual = page.title()

    request.node.user_properties.append(("test_id", test_id))
    request.node.user_properties.append(("scenario", scenario))
    request.node.user_properties.append(("description", description))
    request.node.user_properties.append(("steps", steps))
    request.node.user_properties.append(("expected", expected))
    request.node.user_properties.append(("actual", actual))

    expect(page).to_have_title(expected)


def test_login_page_url(page: Page, request):
    test_id = "TC_002"
    scenario = "Verify Login Page URL"
    description = "Verify that the login page URL is correct."
    steps = "1. Open login page\n2. Verify current URL"
    expected = "https://the-internet.herokuapp.com/login"

    page.goto(expected)

    actual = page.url

    request.node.user_properties.append(("test_id", test_id))
    request.node.user_properties.append(("scenario", scenario))
    request.node.user_properties.append(("description", description))
    request.node.user_properties.append(("steps", steps))
    request.node.user_properties.append(("expected", expected))
    request.node.user_properties.append(("actual", actual))

    expect(page).to_have_url(expected)