import re
from datetime import datetime

TIMESTAMP_PATTERN = r"\d{4}-\d{2}-\d{2}_\d{2}-\d{2}-\d{2}"


def extract_timestamp(key: str):
    match = re.search(TIMESTAMP_PATTERN, key)
    if not match:
        return None

    try:
        return datetime.strptime(match.group(), "%Y-%m-%d_%H-%M-%S")
    except:
        return None


def get_latest_key(keys: list):
    valid = []

    for key in keys:
        ts = extract_timestamp(key)
        if ts:
            valid.append((key, ts))

    if not valid:
        return None

    valid.sort(key=lambda x: x[1], reverse=True)
    return valid[0][0]
