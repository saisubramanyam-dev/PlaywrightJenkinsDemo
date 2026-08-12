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

    if report.when == "call":
        test_name = item.name
        data = TEST_DATA.get(test_name, {})

        report.test_id = data.get("test_id", "")
        report.scenario = data.get("scenario", "")
        report.description = data.get("description", "")
        report.steps = data.get("steps", "")
        report.expected = data.get("expected", "")

        # Actual result
        if report.passed:
            if test_name == "test_login_page_title":
                report.actual = "The Internet"
            elif test_name == "test_login_page_url":
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
    steps = report.steps.replace("\n", "<br>")

    cells.insert(2, f"<td>{report.test_id}</td>")
    cells.insert(3, f"<td>{report.scenario}</td>")
    cells.insert(4, f"<td>{report.description}</td>")
    cells.insert(5, f"<td>{steps}</td>")
    cells.insert(6, f"<td>{report.expected}</td>")
    cells.insert(7, f"<td>{report.actual}</td>")