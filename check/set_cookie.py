from .model import PASS, MISCONFIG, EXPOSED, MISSING, CheckResult

def check_set_cookie(headers):
    return CheckResult(
        status="FAIL",
        details="Set-Cookie flags (Secure/HttpOnly/SameSite) check not implemented yet",
    )
