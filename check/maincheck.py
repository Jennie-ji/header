# check/maincheck.py
from .model import CheckResult
from .x_content_type_options import check_x_content_type_options
from .x_frame_options import check_x_frame_options

CHECKS = {
    "X-Content-Type-Options": check_x_content_type_options,
    "X-Frame-Options": check_x_frame_options,
}

def run_all(headers):
    results = {}
    for name, fn in CHECKS.items():
        try:
            results[name] = fn(headers)
        except Exception as exc:
            results[name] = CheckResult(
                status="FAIL",
                details=f"{name}: exception - {exc}"
            )
    return results
