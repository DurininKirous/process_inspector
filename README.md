# 🧩 process_inspector

A lightweight Python command-line tool for inspecting and analyzing processes on Linux — a simple yet powerful `ps`-like utility.
It reads information directly from the `/proc` filesystem, gathers process statistics, and provides flexible sorting, filtering, and output formatting.

---

## 🚀 Features

* Reads process data directly from `/proc/[pid]`
* Displays a formatted table with key metrics:

  * `PID`, `CPU%`, `MEM%`, `VmPeak`, `VmSize`, `VmHWM`, `VmRSS`, `VmSwap`, `Comm`, `Cmd`
* Supports:

  * Sorting by specific fields (`--sort`)
  * Reverse order (`--reverse`)
  * Limiting output to top N processes (`--top`)
  * Viewing a single process by PID (`--pid`)
  * Human-readable output for memory fields (`--human`)
  * Continuous refresh mode (`--watch N`) — like `top`
  * Multiple output formats: `table` (default), `json`, `csv`
* Clean modular architecture: **gather → analyze → print**

---

## ⚙️ Installation

```bash
git clone https://github.com/DurininKirous/process_inspector.git
cd process_inspector
python3 main.py
```

---

## 🧭 Usage

```bash
python3 main.py [options]
```

### Options

| Option          | Description                                              |
| :-------------- | :------------------------------------------------------- |
| `--sort FIELD`  | Sort output by the given field (`pid`, `vmrss`, `utime`) |
| `--reverse`     | Reverse sort order                                       |
| `--top N`       | Show only the first N processes                          |
| `--pid PID`     | Show information for a single process                    |
| `--human`       | Display memory values in MB instead of bytes             |
| `--format TYPE` | Output format: `table` (default), `json`, or `csv`       |
| `--watch N`     | Refresh every N seconds (like `top`)                     |

---

### Examples

```bash
# Show all processes sorted by memory usage
python3 main.py --sort vmrss

# Show top 10 processes in human-readable format
python3 main.py --sort vmrss --top 10 --human

# Display a specific process
python3 main.py --pid 1234

# Monitor CPU and memory usage live (refresh every 2s)
python3 main.py --sort cpu_percent --watch 2
```

---

### Example Output

```
    PID    CPU%    MEM%     VMPEAK     VMSIZE      VMHWM      VMRSS     VMSWAP   COMM             CMD
==============================================================================================================================
    2022     2.4    16.8 64675.0 MB 48323.6 MB  3171.4 MB  2585.7 MB        N/A Web Content      /usr/lib/firefox/firefox -contentproc -i
    1760     0.5     8.3 29303.8 MB 12922.7 MB  1310.0 MB  1269.8 MB        N/A firefox          /usr/lib/firefox/firefox
```

---

## 🧩 Project Structure

```
process_inspector/
├── main.py
├── cli.py
├── core/
│   ├── process.py
│   ├── gather_processes.py
│   ├── analyze_processes.py
│   ├── print_processes.py
│   └── unitconv.py
└── tests/
    └── test_unitconv.py
```

---

## ⚙️ Design Overview

* **`core/process.py`** — parses individual `/proc/[pid]` entries
* **`core/gather_processes.py`** — collects all processes and reads their stats
* **`core/analyze_processes.py`** — handles sorting and data preparation
* **`core/print_processes.py`** — formats and outputs results (table, JSON, CSV)
* **`cli.py`** — argument parsing
* **`main.py`** — entry point and control flow

---

## 🛠️ Requirements

* Python 3.8+
* Linux-based system (requires `/proc`)
