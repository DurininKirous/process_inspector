import core.analyze_processes as analyze
import core.gather_processes as proc
import core.print_processes as print_processes
from cli import get_args
import time, os

CLK_TCK = os.sysconf("SC_CLK_TCK")

def calculate_cpu(delta_utime, delta_stime, delta_time):
    """Вычисляет процент загрузки CPU"""
    if delta_time <= 0:
        return 0.0
    return 100.0 * (delta_utime + delta_stime) / (CLK_TCK * delta_time)


def get_mem_total_kb() -> int:
    """Считывает общий объём памяти из /proc/meminfo (в килобайтах)"""
    try:
        with open("/proc/meminfo") as f:
            for line in f:
                if line.startswith("MemTotal:"):
                    return int(line.split()[1])
    except FileNotFoundError:
        pass
    return 1 


def run_iteration(args, previous_stats=None, mem_total_kb=None):
    """Одна итерация сбора, анализа и вывода"""
    processes = proc.gather_process_fields()
    processes_output = list(processes.values())

    if mem_total_kb:
        for p in processes_output:
            if p.vmrss:
                p.mem_percent = (int(p.vmrss) / (mem_total_kb * 1024)) * 100  
            else:
                p.mem_percent = 0.0

    if previous_stats is not None:
        current_time = time.time()
        for p in processes_output:
            if not p.utime or not p.stime:
                p.cpu_percent = 0.0
                continue

            pid = p.pid
            if pid in previous_stats:
                prev = previous_stats[pid]
                delta_utime = int(p.utime) - prev["utime"]
                delta_stime = int(p.stime) - prev["stime"]
                delta_time = current_time - prev["timestamp"]
                p.cpu_percent = calculate_cpu(delta_utime, delta_stime, delta_time)
            else:
                p.cpu_percent = 0.0

            previous_stats[pid] = {
                "utime": int(p.utime),
                "stime": int(p.stime),
                "timestamp": current_time
            }

    if args.sort:
        processes_output = analyze.sort(processes_output, args.sort, args.reverse)

    if args.pid:
        single_proc = processes.get(args.pid)
        if single_proc:
            print_processes.output([single_proc], args.format, args.top, args.human, args.pid)
        else:
            print("Process with entered PID doesn't exist!")
    else:
        print_processes.output(processes_output, args.format, args.top, args.human, args.pid)

    return processes


def run_watch_loop(interval, args):
    """Режим постоянного обновления (аналог top)"""
    previous_stats = {}
    mem_total_kb = get_mem_total_kb()

    try:
        while True:
            os.system("clear")
            run_iteration(args, previous_stats, mem_total_kb)
            print(f"Updated at {time.strftime('%H:%M:%S')}")
            time.sleep(interval)
    except KeyboardInterrupt:
        print("\nStopped by user.")


def main():
    args = get_args()
    if args.watch:
        run_watch_loop(args.watch, args)
    else:
        run_iteration(args)


if __name__ == "__main__":
    main()

__version__ = "1.0.0"
