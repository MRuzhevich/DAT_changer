import os
import pytest
import pathlib

from src import file_parser, c_formulas


@pytest.fixture
def test_files():
    directory = "test/test_data"
    file_paths = []  # List which will store all of the full filepaths.

    # Walk the tree.
    for root, directories, files in os.walk(directory):
        for filename in files:
            # Join the two strings in order to form the full filepath.
            filepath = os.path.join(root, filename)
            file_paths.append(pathlib.Path(filepath))  # Add it to the list.

    return file_paths


def test_parse_file(test_files: list[pathlib.Path]):
    os.makedirs(
        test_files[0].parent.parent / "out",
        exist_ok=True,
    )
    for file in test_files:
        file_out = file.parent.parent / "out" / file.name
        file_parser.handle_file(file, file_out, c_formulas.simple_sum)
