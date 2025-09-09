import pytest
from check.x_content_type_options import check_x_content_type_options
from check.model import PASS, MISCONFIG, MISSING, EXPOSED

CASES = [
    ("xcto valid nosniff",
     {"X-Content-Type-Options": "nosniff"},
     {"status": PASS, "found_value": "nosniff"}),
     ("xcto valid nosniff",
     {"X-Content-Type-Options": "Nosniff"},
     {"status": PASS, "found_value": "Nosniff"}),
    ("xcto invalid nosniff",
     {"X-Content-Type-Options": "xxx"},
     {"status": MISCONFIG, "details":"Must be exactly 'nosniff'", "found_value": "xxx"}),
    ("xcto missing",
     {},
     {"status": MISSING,"details":"X-Content-Type-Options header missing", "found_value": None}),
]

@pytest.mark.parametrize("name, headers, expected", CASES)
def test_x_content_type_options(name,headers,expected):
    res = check_x_content_type_options(headers)
    assert res.status == expected["status"]
    if "details" in expected:
        assert res.details == expected["details"]
    assert res.found_value == expected["found_value"]
