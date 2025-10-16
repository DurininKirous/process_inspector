import core.analyze_processes as analyze
import core.gather_processes as proc
import core.print_processes as print_processes
from cli import get_args 

def main():
    args = get_args()
    processes = proc.gather_process_fields()
    processes_output = list(processes.values())
    if args.sort:
        processes_output = analyze.sort(processes_output, args.sort, args.reverse)

    if args.pid:
        single_proc = processes.get(args.pid)
        if single_proc:
            print_processes.output([single_proc], args.top, args.human, args.pid)
        else:
            print("Process with entered PID doesn't exists!")
    else:
        print_processes.output(processes_output, args.top, args.human, args.pid)


if __name__ == "__main__":
    main()
