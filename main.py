import core.analyze_processes as analyze
import core.gather_processes as proc
import core.print_processes as print_processes
from cli import get_args 

def main():
    args = get_args()
    processes = proc.gather_process_fields()
    processes_output = list(processes.values())
    processes_output = analyze.sort_processes(processes_output, args.sort, args.reverse)
    print_processes.title_show()
    for i in processes_output:
        print_processes.print_process(i)

if __name__ == "__main__":
    main()
