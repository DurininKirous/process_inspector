from process import Process

def sort_processes(processes, key) -> list[Process]:
    list_processes = list(processes.values())
    sorted_processes = sorted(list_processes, key = lambda p: getattr(p, key))
    return sorted_processes
