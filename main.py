import core.analyze_processes as analyze
import core.gather_processes as proc
import core.print_processes as print_processes

def main():
    processes = proc.gather_process_fields()
    sorted_processes = analyze.sort_processes(processes, "pid")
    print_processes.title_show()
    for i in sorted_processes:
        print_processes.print_process(i)

if __name__ == "__main__":
    main()
