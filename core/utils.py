from datetime import datetime


def extract_timestamp_from_key(key: str):
    """Assumes format: backups/dbname-YYYY-MM-DD_HH-MM-SS.dump"""
    try:
        filename = key.split("/")[-1]
        ts_part = (
            filename.split("-")[-2] + "-" + filename.split("-")[-1].replace(".dump", "")
        )
        return datetime.strptime(ts_part, "%Y-%m-%d_%H-%M-%S")

    except Exception:
        return None


def get_latest_key(keys: list):
    valid = []
    for key in keys:
        ts = extract_timestamp_from_key(key)
        if ts:
            valid.append((key, ts))
        if not valid:
            return None
        valid.sort(key=lambda x: x[1], reverse=True)
        return valid[0][0]
