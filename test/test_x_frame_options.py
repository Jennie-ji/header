import pytest
from check.x_frame_options import check_x_frame_options
from check.model import PASS, MISCONFIG, MISSING

CASES = [
    ("xfo valid DENY",
     {"X-Frame-Options": "DENY"},
     {"status": PASS, "found_value": "DENY"}),

    ("xfo valid SAMEORIGIN",
     {"X-Frame-Options": "SAMEORIGIN"},
     {"status": PASS, "found_value": "SAMEORIGIN"}),

    ("xfo misconfig repeated tokens",
     {"X-Frame-Options": "SAMEORIGIN, SAMEORIGIN"},
     {"status": MISCONFIG, "details": "No duplicates; use single 'DENY' or 'SAMEORIGIN'", "found_value": "SAMEORIGIN, SAMEORIGIN"}),

    ("xfo misconfig invalid token",
     {"X-Frame-Options": "xxx"},
     {"status": MISCONFIG, "details": "Use 'DENY' or 'SAMEORIGIN'", "found_value": "xxx"}),

    ("xfo missing",
     {},
     {"status": MISSING, "details": "X-Frame-Options missing", "found_value": None}),
]

@pytest.mark.parametrize("name, headers, expected", CASES)
def test_x_frame_options(name, headers, expected):
    res = check_x_frame_options(headers)
    assert res.status == expected["status"]
    if "details" in expected:
        assert res.details == expected["details"]
    assert res.found_value == expected["found_value"]
