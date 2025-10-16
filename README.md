# 🧩 process_inspector

A lightweight Python command-line tool for inspecting and analyzing processes on Linux — a simple `ps`-like utility.
It reads information directly from the `/proc` filesystem, gathers process statistics,
and provides flexible sorting, filtering, and human-readable output options.

---

## 🚀 Features

* Reads process data directly from `/proc/[pid]`
* Displays a formatted table with key metrics:

  * `PID`, `VmPeak`, `VmSize`, `VmHWM`, `VmRSS`, `VmSwap`, `Utime`, `Stime`, `Comm`, `Cmd`
* Supports:

  * Sorting by specific fields (`--sort`)
  * Reverse order (`--reverse`)
  * Limiting output to top N processes (`--top`)
  * Viewing a single process by PID (`--pid`)
  * Human-readable output for memory fields (`--human`)
* Clean modular architecture: **gather → analyze → print**

---

## ⚙️ Installation

```bash
git clone https://github.com/<your_username>/process_inspector.git
cd process_inspector
python3 main.py
```

---

## 🧭 Usage

```bash
python3 main.py [options]
```

### Options

| Option         | Description                                              |
| :------------- | :------------------------------------------------------- |
| `--sort FIELD` | Sort output by the given field (`pid`, `vmrss`, `utime`) |
| `--reverse`    | Reverse sort order                                       |
| `--top N`      | Show only the first N processes                          |
| `--pid PID`    | Show information for a single process                    |
| `--human`      | Display memory values in MB instead of bytes             |

### Examples

```bash
# Show all processes sorted by memory usage
python3 main.py --sort vmrss

# Show top 10 processes in human-readable format
python3 main.py --sort vmrss --top 10 --human

# Display a specific process
python3 main.py --pid 1234
```

---

## 🧩 Project Structure

```
process_inspector/
├── main.py
├── cli.py
└── core/
    ├── process.py
    ├── gather_processes.py
    ├── analyze_processes.py
    ├── print_processes.py
    └── unitconv.py
```

---

## 🛠️ Requirements

* Python 3.8+
* Linux-based system (uses `/proc`)
