UNIT_MAP = {
    "B": 1,
    "kB": 1024,
    "KB": 1024,
    "mB": 1024*1024,
    "MB": 1024*1024
}

def to_bytes(value):
    if not value:
        return 0
    parts = value.split()
    try:
        val = int(parts[0])
    except (IndexError, ValueError):
        return 0
    unit = parts[1] if len(parts) > 1 else "B"
    return val * UNIT_MAP.get(unit, 1)
