from process import Process
import os

def get_processes(proc_path: str = "/proc") -> dict[int, Process]:
    processes = {}
    with os.scandir(proc_path) as entries:
        for entry in entries:
            if entry.is_dir() and entry.name.isdigit():
                processes[entry.name] = Process(int(entry.name), entry.path)
    return processes

def update_processes(proc_path: str = "/proc"):
    processes = get_processes(proc_path)
    for pid, proc in processes.items():
        proc.load()
        print(proc.full_path, " ", proc.pid, " ", proc.cmdline)
