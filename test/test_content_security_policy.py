import pytest
from check.content_security_policy import check_content_security_policy
from check.model import PASS, MISCONFIG, MISSING

CASES = [
    ("csp baseline",
     {"Content-Security-Policy": "default-src 'self'; object-src 'none'; frame-ancestors 'none'"},
     {"status": PASS,
      "found_value": "default-src 'self'; object-src 'none'; frame-ancestors 'none'"}),

    ("csp missing",
     {},
     {"status": MISSING,
      "details": "Add CSP: default-src 'self'; object-src 'none'; frame-ancestors 'none'.",
      "found_value": None}),

    ("csp unsafe directive",
     {"Content-Security-Policy": "default-src 'self'; script-src 'unsafe-inline'"},
     {"status": MISCONFIG,
      "details": "Remove unsafe-*; use nonce/hash.",
      "found_value": "default-src 'self'; script-src 'unsafe-inline'"}),

    ("csp unsafe source",
     {"Content-Security-Policy": "default-src *"},
     {"status": MISCONFIG,
      "details": "Avoid '*'; use 'self' or allowlists.",
      "found_value": "default-src *"}),

    ("csp missing directive",
     {"Content-Security-Policy": "default-src 'self'; frame-ancestors 'none'"},
     {"status": MISCONFIG,
      "details": "Add object-src 'none'.",
      "found_value": "default-src 'self'; frame-ancestors 'none'"}),
]




@pytest.mark.parametrize("name, headers, expected", CASES)
def test_csp(name, headers, expected):
    res = check_content_security_policy(headers)
    assert res.status == expected["status"]
    if "details" in expected:
        assert res.details == expected["details"]
    assert res.found_value == expected["found_value"]
