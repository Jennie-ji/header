from .model import PASS, MISCONFIG, MISSING, EXPOSED, CheckResult

def check_x_frame_options(headers):
    return CheckResult(
        status="FAIL",
        details="X-Frame-Options check not implemented yet",
    )