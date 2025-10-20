import shutil
import json
import csv
import sys
from core.unitconv import format_value

def header():
    header = (
        f"{'PID':>8} {'CPU%':>7} {'MEM%':>7} "
        f"{'VMPEAK':>10} {'VMSIZE':>10} {'VMHWM':>10} {'VMRSS':>10} {'VMSWAP':>10}   "  
        f"{'COMM':<18} {'CMD':<40}"
    )
    width = shutil.get_terminal_size((80, 20)).columns
    number_of_symbols = min(len(header), width)
    print(header)
    print("=" * number_of_symbols)


def process(proc, human: bool = False):
    comm = (proc.comm or "N/A")[:18]
    cmd = (proc.cmdline or "N/A")[:40]
    cpu = getattr(proc, "cpu_percent", 0.0)
    mem = getattr(proc, "mem_percent", 0.0)

    print(
        f"{proc.pid:>8} {cpu:>7.1f} {mem:>7.1f} "
        f"{format_value(proc.vmpeak, human):>10} {format_value(proc.vmsize, human):>10} "
        f"{format_value(proc.vmhwm, human):>10} {format_value(proc.vmrss, human):>10} "
        f"{format_value(proc.vmswap, human):>10}   " 
        f"{comm:<18} {cmd:<40}"
    )

def output(processes, format: str="table", top: int=-1, human: bool=False, pid: int=0):
    if format == "table":
        output_table(processes, top, human, pid)
    elif format == "json":
        output_json(processes, top, human, pid)
    elif format == "csv":
        output_csv(processes, top, human, pid)

def output_table(processes, top: int=-1, human: bool=False, pid: int=0):
    header()
    items = processes[:top] if top >= 0 else processes
    for i in items:
        process(i, human)

def output_json(processes, top: int=-1, human: bool=False, pid: int=0):
    data = []
    items = processes[:top] if top >= 0 else processes
    for p in items:
        data.append({
            "pid": p.pid,
            "cpu_percent": getattr(p, "cpu_percent", 0.0),
            "mem_percent": getattr(p, "mem_percent", 0.0),
            "vmpeak": format_value(p.vmpeak, human),
            "vmsize": format_value(p.vmsize, human),
            "vmhwm": format_value(p.vmhwm, human),
            "vmrss": format_value(p.vmrss, human),
            "vmswap": format_value(p.vmswap, human),
            "comm": p.comm,
            "cmdline": p.cmdline,
        })
    print(json.dumps(data, indent=4))

def output_csv(processes, top: int=-1, human: bool=False, pid: int=0):
    items = processes[:top] if top >= 0 else processes
    fieldnames = [
        "pid", "cpu_percent", "mem_percent", "comm", "cmdline",
        "vmpeak", "vmsize", "vmhwm", "vmrss", "vmswap"
    ]
    writer = csv.DictWriter(sys.stdout, fieldnames=fieldnames)
    writer.writeheader()
    for p in items:
        writer.writerow({
            "pid": p.pid,
            "cpu_percent": getattr(p, "cpu_percent", 0.0),
            "mem_percent": getattr(p, "mem_percent", 0.0),
            "comm": p.comm,
            "cmdline": p.cmdline,
            "vmpeak": format_value(p.vmpeak, human),
            "vmsize": format_value(p.vmsize, human),
            "vmhwm": format_value(p.vmhwm, human),
            "vmrss": format_value(p.vmrss, human),
            "vmswap": format_value(p.vmswap, human),
        })

