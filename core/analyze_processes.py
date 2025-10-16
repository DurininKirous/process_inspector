from core.process import Process

def sort(processes, key, reverse) -> list[Process]:
    valid = [p for p in processes if getattr(p, key) is not None]
    return sorted(valid, key=lambda p: getattr(p, key), reverse = reverse)
