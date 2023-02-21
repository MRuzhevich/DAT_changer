from pathlib import Path

from src import file_browser as fb
from src import file_parser, c_formulas


def main():
    files = fb.FileBrowser()
    out_dir = file_parser.get_out_dir(Path(files.filenames[0]))
    for file in files.filenames:
        file_in = Path(file)
        file_out = out_dir / file_in.name
        file_parser.handle_file(file_in, file_out, c_formulas.simple_sum)


if __name__ == "__main__":
    main()
