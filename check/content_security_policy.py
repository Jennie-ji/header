from .model import PASS, MISCONFIG, MISSING, EXPOSED, CheckResult

def check_content_security_policy(headers):
    return CheckResult(
        status="FAIL",
        details="Content-Security-Policy check not implemented yet",
    )
