from dataclasses import dataclass

PASS = "PASS"
MISSING = "Not found but should exist"
EXPOSED = "Found but should not exist"
MISCONFIG = "Found but misconfig"

@dataclass
class CheckResult:
    status: str
    details: str = ""
    found_value: str | None = None
