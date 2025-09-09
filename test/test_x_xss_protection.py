import pytest
from check.x_xss_protection import check_x_xss_protection
from check.model import PASS, MISCONFIG

CASES = [
    ("xxp misconfig mode=block",
     {"X-XSS-Protection": "1; mode=block"},
     {"status": MISCONFIG, "details": "X-XSS-Protection must be absent or '0'", "found_value": "1; mode=block"}),

    ("xxp valid disabled",
     {"X-XSS-Protection": "0"},
     {"status": PASS, "found_value": "0"}),

    ("xxp misconfig no_mode",
     {"X-XSS-Protection": "1"},
     {"status": MISCONFIG, "details": "X-XSS-Protection must be absent or '0'", "found_value": "1"}),

    ("xxp missing",
     {},
     {"status": PASS, "found_value": None}),
]

@pytest.mark.parametrize("name, headers, expected", CASES)
def test_x_xss_protection(name, headers, expected):
    res = check_x_xss_protection(headers)
    assert res.status == expected["status"]
    if "details" in expected:
        assert res.details == expected["details"]
    assert res.found_value == expected["found_value"]
