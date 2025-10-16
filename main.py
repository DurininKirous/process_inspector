import core.analyze_processes as analyze
import core.gather_processes as proc
import core.print_processes as print_processes
from cli import get_args 
import time, os

def run_iteration(args):
    processes = proc.gather_process_fields()
    processes_output = list(processes.values())

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

def run_watch_loop(interval, args):
    try:
        while True:
            os.system("clear")
            run_iteration(args)
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

