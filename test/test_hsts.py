import pytest
from check.hsts import check_hsts
from check.model import PASS, MISCONFIG, MISSING

CASES = [
    ("hsts valid min one year + includeSubDomains",
     {"Strict-Transport-Security": "max-age=31536000; includeSubDomains; preload"},
     {"status": PASS, "found_value": "max-age=31536000; includeSubDomains; preload"}),

    ("hsts PASS order swapped",
     {"Strict-Transport-Security": "max-age=31536000; includeSubDomains"},
     {"status": PASS, "found_value": "max-age=31536000; includeSubDomains"}),

    ("hsts PASS long max-age 2y",
     {"Strict-Transport-Security": "includeSubDomains; max-age=31536000"},
     {"status": PASS, "found_value": "includeSubDomains; max-age=31536000"}),

    ("hsts invalid low max-age",
     {"Strict-Transport-Security": "max-age=86400"},
     {"status": MISCONFIG,
      "details": "Use max-age ≥ 31536000 and includeSubDomains.",
      "found_value": "max-age=86400"}),

    ("hsts invalid missing includeSubDomains",
     {"Strict-Transport-Security": "max-age=31536000"},
     {"status": MISCONFIG,
      "details": "Add includeSubDomains.",
      "found_value": "max-age=31536000"}),

    ("hsts missing",
     {},
     {"status": MISSING,
      "details": "Add HSTS: max-age ≥ 31536000; includeSubDomains.",
      "found_value": None}),
]

@pytest.mark.parametrize("name, headers, expected", CASES)
def test_hsts(name, headers, expected):
    res = check_hsts(headers)
    assert res.status == expected["status"]
    if "details" in expected:
        assert res.details == expected["details"]
    assert res.found_value == expected["found_value"]
