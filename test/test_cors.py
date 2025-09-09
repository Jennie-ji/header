import pytest
from check.cors import check_cors_policy
from check.model import PASS, MISCONFIG, MISSING

CASES = [
    ("cors valid allowlist + no credentials",
     {"Access-Control-Allow-Origin": "https://test.com", "Access-Control-Allow-Credentials": "false"},
     {"status": PASS, "found_value": "https://test.com"}),

    ("cors invalid wildcard origin",
     {"Access-Control-Allow-Origin": "*"},
     {"status": MISCONFIG,
      "details": "Use explicit origin.",
      "found_value": "*"}),

    ("cors invalid credentials true",
     {"Access-Control-Allow-Origin": "https://any.com", "Access-Control-Allow-Credentials": "true"},
     {"status": MISCONFIG,
      "details": "Set credentials=false.",
      "found_value": "https://any.com"}),

    ("cors wildcard with credentials not pass",
     {"Access-Control-Allow-Origin": "*", "Access-Control-Allow-Credentials": "true"},
     {"status": MISCONFIG,
      "details": "No '*' with credentials.",
      "found_value": "*"}),

    ("cors not_used_no_headers",
     {},
     {"status": MISSING,
      "details": "Add Access-Control-Allow-Origin.",
      "found_value": None}),
]

@pytest.mark.parametrize("name, headers, expected", CASES)
def test_cors_policy(name, headers, expected):
    res = check_cors_policy(headers)
    assert res.status == expected["status"]
    if "details" in expected:
        assert res.details == expected["details"]
    assert res.found_value == expected["found_value"]
