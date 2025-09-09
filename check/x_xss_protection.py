from .model import PASS, MISCONFIG, MISSING, EXPOSED, CheckResult

def check_x_xss_protection(headers):
    return CheckResult(
        status="FAIL",
        details="X-XSS-Protection check not implemented yet",
    )
