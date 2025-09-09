import pytest
from check.set_cookie import check_set_cookie
from check.model import PASS, MISCONFIG, MISSING

CASES = [
    ("Set-Cookie OK (Strict)",
     {"Set-Cookie": "sid=abc; Secure; HttpOnly; SameSite=Strict"},
     {"status": PASS, "found_value": "sid=abc; Secure; HttpOnly; SameSite=Strict"}),

    ("missing header -> MISSING",
     {},
     {"status": MISSING, "details": "Set-Cookie header missing", "found_value": None}),

    ("missing Secure",
     {"Set-Cookie": "sid=abc; HttpOnly; SameSite=Strict"},
     {"status": MISCONFIG, "details": "Cookie missing flags: Secure",
      "found_value": "sid=abc; HttpOnly; SameSite=Strict"}),

    ("missing HttpOnly",
     {"Set-Cookie": "sid=abc; Secure; SameSite=Strict"},
     {"status": MISCONFIG, "details": "Cookie missing flags: HttpOnly",
      "found_value": "sid=abc; Secure; SameSite=Strict"}),

    ("missing SameSite=Strict",
     {"Set-Cookie": "sid=abc; Secure; HttpOnly"},
     {"status": MISCONFIG, "details": "Cookie missing flags: SameSite=Strict",
      "found_value": "sid=abc; Secure; HttpOnly"}),

    ("SameSite=None MISCONFIG",
     {"Set-Cookie": "sid=abc; Secure; HttpOnly; SameSite=None"},
     {"status": MISCONFIG, "details": "Cookie missing flags: samesite=strict",
      "found_value": "sid=abc; Secure; HttpOnly; SameSite=None"}),

    ("multi cookies: one missing flag -> MISCONFIG",
     {"Set-Cookie": "sid=abc; Secure; HttpOnly; SameSite=Strict\nprefs=xyz; HttpOnly; SameSite=Lax"},
     {"status": MISCONFIG, "details": "Cookie missing flags: Secure",
      "found_value": "sid=abc; Secure; HttpOnly; SameSite=Strict\nprefs=xyz; HttpOnly; SameSite=Lax"}),
]

@pytest.mark.parametrize("name, headers, expected", CASES)
def test_set_cookie(name, headers, expected):
    res = check_set_cookie(headers)
    assert res.status == expected["status"]
    if "details" in expected:
        assert res.details == expected["details"]
    assert res.found_value == expected["found_value"]
