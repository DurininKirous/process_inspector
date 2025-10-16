import shutil

def title_show():
    header = f"{'PID':>8} {'VMPEAK':>10} {'VMSIZE':>10} {'VMHWM':>10} {'VMRSS':>10} {'VMSWAP':>10} {'UTIME':>10} {'STIME':>10}   {'COMM':<16} {'CMD':<40}"
    width = shutil.get_terminal_size((80, 20)).columns
    number_of_symbols = min(len(header), width)
    print(header)
    print("="*number_of_symbols)

def print_process(proc):
    fmt = lambda x: str(x) if x is not None else "N/A"
    
    # Обрезаем длинные значения
    comm = (proc.comm or "N/A")[:10]
    cmd = fmt(proc.cmdline)[:15]
    
    print(f"{proc.pid:>8} {fmt(proc.vmpeak):>10} {fmt(proc.vmsize):>10} {fmt(proc.vmhwm):>10} "
          f"{fmt(proc.vmrss):>10} {fmt(proc.vmswap):>10} {fmt(proc.utime):>10} {fmt(proc.stime):>10} "
          f"  {comm:<16} {cmd:<40}")
