import pytest
from check.referrer import check_referrer
from check.model import PASS, MISCONFIG, MISSING

CASES = [
    ("rp valid no-referrer",
     {"Referrer-Policy": "no-referrer"},
     {"status": PASS, "found_value": "no-referrer"}),

    ("rp invalid unsafe-url",
     {"Referrer-Policy": "unsafe-url"},
     {"status": MISCONFIG, "details": "Use 'no-referrer'.", "found_value": "unsafe-url"}),

    ("rp missing",
     {},
     {"status": MISSING, "details": "Add Referrer-Policy header with 'no-referrer'.", "found_value": None}),
]

@pytest.mark.parametrize("name, headers, expected", CASES)
def test_referrer(name, headers, expected):
    res = check_referrer(headers)
    assert res.status == expected["status"]
    if "details" in expected:
        assert res.details == expected["details"]
    assert res.found_value == expected["found_value"]
