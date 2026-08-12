import pytest


TEST_DATA = {
    "test_login_page_title": {
        "test_id": "TC_001",
        "scenario": "Verify Login Page Title",
        "description": "Verify that the login page displays the correct title.",
        "steps": "1. Open login page\n2. Verify page title",
        "expected": "The Internet",
    },
    "test_login_page_url": {
        "test_id": "TC_002",
        "scenario": "Verify Login Page URL",
        "description": "Verify that the login page URL is correct.",
        "steps": "1. Open login page\n2. Verify current URL",
        "expected": "https://the-internet.herokuapp.com/login",
    },
}


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    # Only attach our custom data to the actual test execution
    if report.when == "call":
        data = TEST_DATA.get(item.name, {})

        report.test_id = data.get("test_id", "")
        report.scenario = data.get("scenario", "")
        report.description = data.get("description", "")
        report.steps = data.get("steps", "")
        report.expected = data.get("expected", "")

        if report.passed:
            if item.name == "test_login_page_title":
                report.actual = "The Internet"
            elif item.name == "test_login_page_url":
                report.actual = "https://the-internet.herokuapp.com/login"
            else:
                report.actual = "PASS"
        else:
            report.actual = "Test Failed"


def pytest_html_results_table_header(cells):
    cells.insert(2, "<th>Test ID</th>")
    cells.insert(3, "<th>Scenario</th>")
    cells.insert(4, "<th>Description</th>")
    cells.insert(5, "<th>Test Steps</th>")
    cells.insert(6, "<th>Expected Result</th>")
    cells.insert(7, "<th>Actual Result</th>")


def pytest_html_results_table_row(report, cells):
    # Some pytest-html rows are not the actual test-call report.
    # Ignore those rows.
    if not hasattr(report, "test_id"):
        return

    test_id = getattr(report, "test_id", "")
    scenario = getattr(report, "scenario", "")
    description = getattr(report, "description", "")
    steps = getattr(report, "steps", "")
    expected = getattr(report, "expected", "")
    actual = getattr(report, "actual", "")

    steps = steps.replace("\n", "<br>")

    cells.insert(2, f"<td>{test_id}</td>")
    cells.insert(3, f"<td>{scenario}</td>")
    cells.insert(4, f"<td>{description}</td>")
    cells.insert(5, f"<td>{steps}</td>")
    cells.insert(6, f"<td>{expected}</td>")
    cells.insert(7, f"<td>{actual}</td>")