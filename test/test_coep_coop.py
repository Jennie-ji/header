import pytest
from check.coep_coop import check_coep_coop
from check.model import PASS, MISCONFIG, MISSING

CASES = [
    ("isolation ok: coop same-origin + coep require-corp",
     {"Cross-Origin-Opener-Policy": "same-origin",
      "Cross-Origin-Embedder-Policy": "require-corp"},
     {"status": PASS, "found_value": {
         "coop": "same-origin", "coep": "require-corp"}}),

    ("isolation misconfig: coop only",
     {"Cross-Origin-Opener-Policy": "same-origin"},
     {"status": MISCONFIG, "details": "COOP present without COEP (not cross-origin isolated)",
      "found_value": {"coop": "same-origin", "coep": None}}),

    ("isolation misconfig: coep only",
     {"Cross-Origin-Embedder-Policy": "require-corp"},
     {"status": MISCONFIG, "details": "COEP present without COOP (not cross-origin isolated)",
      "found_value": {"coop": None, "coep": "require-corp"}}),

    ("isolation misconfig: invalid coop value",
     {"Cross-Origin-Opener-Policy": "unsafe-none",
      "Cross-Origin-Embedder-Policy": "require-corp"},
     {"status": MISCONFIG, "details": "Invalid COOP; use 'same-origin' or 'same-origin-allow-popups'",
      "found_value": {"coop": "unsafe-none", "coep": "require-corp"}}),

    ("isolation misconfig: invalid coep value",
     {"Cross-Origin-Opener-Policy": "same-origin",
      "Cross-Origin-Embedder-Policy": "xxx"},
     {"status": MISCONFIG, "details": "Invalid COEP; use 'require-corp'",
      "found_value": {"coop": "same-origin", "coep": "xxx"}}),

    ("isolation misconfig: report-only only",
     {"Cross-Origin-Opener-Policy": "same-origin",
      "Cross-Origin-Embedder-Policy-Report-Only": "require-corp; report-to=\"default\""},
     {"status": MISCONFIG, "details": "COEP is Report-Only; enable enforcing 'Cross-Origin-Embedder-Policy: require-corp'",
      "found_value": {"coop": "same-origin", "coep": "report-only"}}),

    ("isolation missing: none",
     {},
     {"status": MISSING, "details": "COOP and COEP missing", "found_value": {"coop": None, "coep": None}}),
]

@pytest.mark.parametrize("name, headers, expected", CASES)
def test_coep_coop(name, headers, expected):
    res = check_coep_coop(headers)
    assert res.status == expected["status"]
    if "details" in expected:
        assert res.details == expected["details"]
    assert res.found_value == expected["found_value"]
