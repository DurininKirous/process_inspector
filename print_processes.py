def title_show():
    print("PID  VMPEAK  VMSIZE  VMHWM  VMEAA  VMSWAP  UTIME  STIME  COMM  CMD")

def print_process(process):
    print(process.pid, " ", process.vmpeak, " ", process.vmsize, " ", process.vmhwm, " ", process.vmrss, " ", process.vmswap, " ", process.utime, " ", process.stime, " ", process.comm, " ", process.cmdline)
