from dataclasses import dataclass
from typing import Optional
from pathlib import Path
import core.unitconv as unitconv

@dataclass
class Process:
    pid:              int
    full_path:        str
    cmdline: Optional[str] = None
    comm:    Optional[str] = None
    vmpeak:  Optional[int] = None
    vmsize:  Optional[int] = None
    vmhwm:   Optional[int] = None
    vmrss:   Optional[int] = None
    vmswap:  Optional[int] = None
    utime:   Optional[int] = None
    stime:   Optional[int] = None

    _status_mapping = {
        "VmPeak": "vmpeak",
        "VmSize": "vmsize",
        "VmHWM":  "vmhwm",
        "VmRSS":  "vmrss",
        "VmSwap": "vmswap"
    }
    
    _stat_mapping = {
        "utime": 14,
        "stime": 15
    }

    def load(self):
        self._load_cmdline()
        self._load_comm()
        self._load_status()
        self._load_stat()

    def _load_cmdline(self):
        try:
            with open(Path(self.full_path) / "cmdline") as f:
                self.cmdline = f.read().replace("\x00", " ").strip()
        except FileNotFoundError:
            pass
        except PermissionError:
            pass

    def _load_comm(self):
        try:
            with open(Path(self.full_path) / "comm") as f:
                self.comm = f.read().rstrip("\n")
        except FileNotFoundError:
            pass
        except PermissionError:
            pass

    def _load_status(self):
        try:
            with open(Path(self.full_path) / "status") as f:
                for line in f:
                    if ":" not in line:
                        continue

                    key, value = line.split(":", 1)
                    key = key.strip()

                    if key in self._status_mapping:
                        value_translated = unitconv.to_bytes(value)
                        attr_name = self._status_mapping[key]
                        setattr(self, attr_name, value_translated)
        except FileNotFoundError:
            pass
        except PermissionError:
            pass

    def _load_stat(self):
        try:
            with open(Path(self.full_path) / "stat") as f:
                stat = f.read()
                parts = stat.split()
                for key, number in self._stat_mapping.items(): 
                    value = parts[number]
                    setattr(self, key, value)
        except FileNotFoundError:
            pass
        except PermissionError:
            pass
