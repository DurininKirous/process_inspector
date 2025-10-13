from dataclasses import dataclass
from typing import Optional
from pathlib import Path

@dataclass
class Process:
    pid:              int
    full_path:        str
    cmdline: Optional[str] = None
    comm:    Optional[str] = None
    VmPeak:  Optional[int] = None
    VmSize:  Optional[int] = None
    VmHWM:   Optional[int] = None
    VmRSS:   Optional[int] = None
    VmSwap:  Optional[int] = None
    utime:   Optional[int] = None
    stime:   Optional[int] = None

    def load(self):
        self._load_cmdline()
#        self._load_comm()
#        self._load_status()
#        self._load_stat()

    def _load_cmdline(self):
        try:
            with open(Path(self.full_path) / "cmdline") as f:
                self.cmdline = f.readline()
        except FileNotFoundError:
            pass
        except PermissionError:
            pass
