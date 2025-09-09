from .model import PASS, MISCONFIG, MISSING, EXPOSED, CheckResult

def check_hsts(headers):
    return CheckResult(
        status="FAIL",
        details="Strict-Transport-Security (HSTS) check not implemented yet",
    )
