from .model import PASS, MISCONFIG, EXPOSED, MISSING, CheckResult

def check_server(headers):
    return CheckResult(
        status="FAIL",
        details="Server disclosure check not implemented yet",
    )
