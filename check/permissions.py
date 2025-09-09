from .model import PASS, MISCONFIG, MISSING, EXPOSED, CheckResult

def check_permissions(headers):
    return CheckResult(
        status="FAIL",
        details="Permissions-Policy check not implemented yet",
    )
