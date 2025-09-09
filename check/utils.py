from typing import Mapping, Optional

def ci_get(headers: Mapping[str, str], key: str) -> Optional[str]:
    for k, v in headers.items():
        if k.lower() == key.lower():
            return v
    return None
