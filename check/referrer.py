from .model import PASS, MISCONFIG, MISSING, EXPOSED, CheckResult

def check_referrer(headers):
    return CheckResult(
        status="FAIL",
        details="Referrer-Policy check not implemented yet",
    )
