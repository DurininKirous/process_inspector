import argparse

def get_args():
    parser = argparse.ArgumentParser(description="описание программы")
    parser.add_argument("--sort", help="поле для сортировки", choices=["pid", "vmrss", "utime"])
    parser.add_argument("--reverse",action="store_true", help="сортировка по возрастанию или убыванию")
    parser.add_argument("--top", type=int, default=-1, help="показать только первые N процессов")
    parser.add_argument("--format", default="table", help="формат вывода процессов", choices=["table", "csv", "json"])
    parser.add_argument("--watch", type=int, default=0, help="постоянный вывод процессов")
    parser.add_argument("--pid", type=int, default=0, help="показать информацию только об одном процессе")
    parser.add_argument("--human", action="store_true", help="показать информацию в человекочитаемом формате")
    return parser.parse_args()
