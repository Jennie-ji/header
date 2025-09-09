import pytest
from check.permissions import check_permissions
from check.model import PASS, MISCONFIG, MISSING

CASES = [
    ("pp valid deny sensitive features",
     {"Permission-Policy": "accelerometer=(), geolocation=(), microphone=()"},
     {"status": PASS, "found_value": "accelerometer=(), geolocation=(), microphone=()"}),

    ("pp invalid wildcard",
     {"Permission-Policy": "geolocation=*, camera=()"},
     {"status": MISCONFIG,
      "details": "Avoid '*'; use explicit values (e.g., geolocation=()).",
      "found_value": "geolocation=*, camera=()"}),

    ("pp missing (empty value)",
     {"Permission-Policy": ""},
     {"status": MISSING,
      "details": "Header empty. Set explicit policy.",
      "found_value": ""}),

    ("pp missing header",
     {},
     {"status": MISSING,
      "details": "Add Permission-Policy with explicit values.",
      "found_value": None}),
]

@pytest.mark.parametrize("name, headers, expected", CASES)
def test_permissions(name, headers, expected):
    res = check_permissions(headers)
    assert res.status == expected["status"]
    if "details" in expected:
        assert res.details == expected["details"]
    assert res.found_value == expected["found_value"]
