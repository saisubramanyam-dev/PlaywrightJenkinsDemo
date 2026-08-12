import pytest


@pytest.hookimpl(optionalhook=True)
def pytest_html_results_table_header(cells):
    cells.insert(2, "<th>Test ID</th>")
    cells.insert(3, "<th>Scenario</th>")
    cells.insert(4, "<th>Description</th>")
    cells.insert(5, "<th>Test Steps</th>")
    cells.insert(6, "<th>Expected Result</th>")
    cells.insert(7, "<th>Actual Result</th>")


@pytest.hookimpl(optionalhook=True)
def pytest_html_results_table_row(report, cells):
    data = dict(report.user_properties)

    cells.insert(2, f"<td>{data.get('test_id', '')}</td>")
    cells.insert(3, f"<td>{data.get('scenario', '')}</td>")
    cells.insert(4, f"<td>{data.get('description', '')}</td>")
    cells.insert(5, f"<td>{data.get('steps', '').replace(chr(10), '<br>')}</td>")
    cells.insert(6, f"<td>{data.get('expected', '')}</td>")
    cells.insert(7, f"<td>{data.get('actual', '')}</td>")