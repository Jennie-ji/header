import pytest
from check.cache_control import check_cache_control
from check.model import PASS, MISCONFIG, MISSING

CASES = [
    ("cache valid no-store",
     {"Cache-Control": "no-store"},
     {"status": PASS, "found_value": "no-store"}),

    ("cache valid no-cache",
     {"Cache-Control": "no-cache"},
     {"status": PASS, "found_value": "no-cache"}),

    ("cc misconfig public",
     {"Cache-Control": "public, max-age=600"},
     {"status": MISCONFIG,
      "details": "Use 'no-store' or 'no-cache'",
      "found_value": "public, max-age=600"}),

    ("cc misconfig max-age only",
     {"Cache-Control": "max-age=3600"},
     {"status": MISCONFIG,
      "details": "Use 'no-store' or 'no-cache'",
      "found_value": "max-age=3600"}),

    ("cc misconfig conflicting",
     {"Cache-Control": "no-store, public"},
     {"status": MISCONFIG,
      "details": "Remove conflicts; prefer a single policy (no-cache or no-store).",
      "found_value": "no-store, public"}),

    ("cache missing",
     {},
     {"status": MISSING,
      "details": "Add Cache-Control: no-store or no-cache.",
      "found_value": None}),
]

@pytest.mark.parametrize("name, headers, expected", CASES)
def test_cache_control(name, headers, expected):
    res = check_cache_control(headers)
    assert res.status == expected["status"]
    if "details" in expected:
        assert res.details == expected["details"]
    assert res.found_value == expected["found_value"]
