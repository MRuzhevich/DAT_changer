from pathlib import Path
from typing import Callable

FILE_SEPARATOR = "\t"


def write_file(filename: str, data: str) -> None:
    with open(filename, "w") as f:
        f.write(data)


def parse_line(line: str) -> list[str]:
    return line.strip().split(FILE_SEPARATOR)


def evaluate_line(line_data: list[str], func: Callable) -> str:
    new_value = str(func(*[int(float(i)) for i in line_data]))
    return FILE_SEPARATOR.join(line_data + [new_value]) + "\n"


def handle_file(
    filename: Path, filename_out: Path, handle_func: Callable
) -> None:
    with open(filename, "r") as f:
        with open(filename_out, "w") as f_out:
            for line in f:
                line_data = parse_line(line)
                f_out.write(evaluate_line(line_data, handle_func))
