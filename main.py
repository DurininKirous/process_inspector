import core.analyze_processes as analyze
import core.gather_processes as proc
import core.print_processes as print_processes
from cli import get_args 

def main():
    args = get_args()
    processes = proc.gather_process_fields()
    processes_output = list(processes.values())
    processes_output = analyze.sort(processes_output, args.sort, args.reverse)
    print_processes.output(processes_output, args.top, args.human)

if __name__ == "__main__":
    main()
