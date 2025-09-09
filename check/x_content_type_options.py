from .model import PASS, MISCONFIG, MISSING, EXPOSED, CheckResult


def check_x_content_type_options(headers):
    
    KEY = "X-Content-Type-Options"
    present = KEY in headers
    if not present:
        return CheckResult(status=MISSING,details="X-Content-Type-Options header missing")

    value = headers.get("X-Content-Type-Options")
    if value == "nosniff":
        return CheckResult(status=PASS, found_value=value)

    return CheckResult(
        status=MISCONFIG,
        details="Must be exactly 'nosniff'",
        found_value=value
    )
    

