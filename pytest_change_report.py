import pytest


def pytest_addoption(parser):
    parser.addoption(
        "--change",
        action="store",
        default="off",
        help="'Default 'off' for change, option: on or off"
    )


def pytest_report_teststatus(report, config):
    '''turn . into √，turn F into x, turn E into 0'''
    if config.getoption("--change") == "on":
        if report.when == 'call' and report.failed:
            return (report.outcome, 'x', 'failed')
        if report.when == 'call' and report.passed:
            return (report.outcome, '√', 'passed')