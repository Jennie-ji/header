from .model import PASS, MISCONFIG, MISSING, EXPOSED, CheckResult

def check_cors_policy(headers):
    return CheckResult(
        status="FAIL",
        details="CORS policy check not implemented yet",
    )
