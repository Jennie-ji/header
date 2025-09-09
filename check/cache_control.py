from .model import PASS, MISCONFIG, MISSING, CheckResult

def check_cache_control(headers):
    return CheckResult(
        status="FAIL",
        details="Cache-Control check not implemented yet",
    )
