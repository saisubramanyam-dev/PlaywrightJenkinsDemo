import html
from pathlib import Path

import pytest


RESULTS = []


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when != "call":
        return

    status = "PASS" if report.passed else "FAIL"

    if report.failed:
        actual = getattr(item, "actual", "Test failed")
    else:
        actual = getattr(item, "actual", "")

    result = {
        "test_id": getattr(item, "test_id", ""),
        "scenario": getattr(item, "scenario", item.name),
        "description": getattr(item, "description", ""),
        "steps": getattr(item, "steps", []),
        "expected": getattr(item, "expected", ""),
        "actual": actual,
        "status": status,
        "duration": f"{report.duration:.2f}s",
    }

    RESULTS.append(result)


def pytest_sessionfinish(session, exitstatus):
    report_file = Path("report.html")

    rows = ""

    for result in RESULTS:
        steps = "<br>".join(
            html.escape(step) for step in result["steps"]
        )

        status_class = (
            "pass"
            if result["status"] == "PASS"
            else "fail"
        )

        rows += f"""
        <tr>
            <td>{html.escape(result["test_id"])}</td>
            <td>{html.escape(result["scenario"])}</td>
            <td>{html.escape(result["description"])}</td>
            <td>{steps}</td>
            <td>{html.escape(result["expected"])}</td>
            <td>{html.escape(result["actual"])}</td>
            <td class="{status_class}">
                {html.escape(result["status"])}
            </td>
            <td>{html.escape(result["duration"])}</td>
        </tr>
        """

    total = len(RESULTS)
    passed = sum(
        1 for result in RESULTS
        if result["status"] == "PASS"
    )
    failed = total - passed

    html_content = f"""
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Playwright Test Report</title>

    <style>
        body {{
            font-family: Arial, sans-serif;
            margin: 30px;
            background-color: #f5f6f7;
        }}

        h1 {{
            color: #222;
        }}

        .summary {{
            display: flex;
            gap: 20px;
            margin: 20px 0;
        }}

        .summary-box {{
            padding: 15px 25px;
            background: white;
            border-radius: 6px;
            border: 1px solid #ddd;
        }}

        table {{
            width: 100%;
            border-collapse: collapse;
            background: white;
        }}

        th {{
            background-color: #333;
            color: white;
            padding: 12px;
            text-align: left;
        }}

        td {{
            padding: 12px;
            border: 1px solid #ddd;
            vertical-align: top;
        }}

        .pass {{
            font-weight: bold;
        }}

        .fail {{
            font-weight: bold;
        }}
    </style>
</head>

<body>

<h1>Playwright Test Execution Report</h1>

<div class="summary">

    <div class="summary-box">
        <strong>Total Tests</strong><br>
        {total}
    </div>

    <div class="summary-box">
        <strong>Passed</strong><br>
        {passed}
    </div>

    <div class="summary-box">
        <strong>Failed</strong><br>
        {failed}
    </div>

</div>

<table>

    <thead>
        <tr>
            <th>Test ID</th>
            <th>Scenario</th>
            <th>Description</th>
            <th>Test Steps</th>
            <th>Expected Result</th>
            <th>Actual Result</th>
            <th>Status</th>
            <th>Duration</th>
        </tr>
    </thead>

    <tbody>
        {rows}
    </tbody>

</table>

</body>
</html>
"""

    report_file.write_text(
        html_content,
        encoding="utf-8"
    )