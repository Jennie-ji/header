import pytest
from check.server import check_server
from check.model import PASS, EXPOSED

CASES = [
    ("no server info",
     {},
     {"status": PASS, "found_value": None}),

    ("has Server header",
     {"Server": "Microsoft-IIS/7.5"},
     {"status": EXPOSED, "details": "Server header should not be exposed", "found_value": "Microsoft-IIS/7.5"}),

    ("has X-Powered-By",
     {"X-Powered-By": "ASP.NET"},
     {"status": EXPOSED, "details": "X-Powered-By header should not be exposed", "found_value": "ASP.NET"}),
]

@pytest.mark.parametrize("name, headers, expected", CASES)
def test_server(name, headers, expected):
    res = check_server(headers)
    assert res.status == expected["status"]
    if "details" in expected:
        assert res.details == expected["details"]
    assert res.found_value == expected["found_value"]
