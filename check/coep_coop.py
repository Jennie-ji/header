from .model import PASS, MISCONFIG, MISSING, EXPOSED, CheckResult

def check_coep_coop(headers):
    return CheckResult(
        status="FAIL",
        details="coep_coop check not implemented yet",
    )
