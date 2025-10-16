import shutil
from core.unitconv import format_value

def header():
    header = f"{'PID':>8} {'VMPEAK':>10} {'VMSIZE':>10} {'VMHWM':>10} {'VMRSS':>10} {'VMSWAP':>10} {'UTIME':>10} {'STIME':>10}   {'COMM':<16} {'CMD':<40}"
    width = shutil.get_terminal_size((80, 20)).columns
    number_of_symbols = min(len(header), width)
    print(header)
    print("="*number_of_symbols)

def process(proc, human: bool=False):
    comm = (proc.comm or "N/A")[:10]
    cmd = (proc.cmdline or "N/A")[:15]
    
    print(f"{proc.pid:>8} {format_value(proc.vmpeak,human):>10} {format_value(proc.vmsize, human):>10} {format_value(proc.vmhwm, human):>10} "
          f"{format_value(proc.vmrss,human):>10} {format_value(proc.vmswap,human):>10} {proc.utime:>10} {proc.stime:>10} "
          f"  {comm:<16} {cmd:<40}")

def output(processes, top: int=0, human: bool=False):
    header()
    count = top
    if count < 0:
        count = -1
    for i in processes[:count]:
        process(i, human)
