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
def to_mbytes(value):
    return value / UNIT_MAP.get("MB", 1)

def format_value(value, human: bool=False):
    if not value:
        return "N/A"
    if human:
        return f"{to_mbytes(value):.1f} MB"
    return str(value)
