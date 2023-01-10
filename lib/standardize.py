import csv
import os
import re
from os import listdir
from os.path import isfile, join
from pathlib import Path

import pandas
import yaml


class CsvFileColumnError(ValueError):
    pass


def format_csv(input_file_name: str, input_separator: str, column_count: int) -> str:
    with open(input_file_name, "r") as f:
        df = pandas.read_csv(f, sep=input_separator)

        if len(df.columns) != column_count:
            raise CsvFileColumnError(
                f"Expected row count is {column_count} got {len(df.columns)}"
            )

        return df.to_csv(
            None, sep=",", quotechar="'", quoting=csv.QUOTE_NONNUMERIC, index=False
        )


def get_data_files(regex: str = "") -> list[str]:
    compiled_regex = re.compile(regex)

    current_dir = get_current_folder()
    path = join(current_dir, "../dataDropArea")

    files = [
        file
        for file in listdir(path)
        if isfile(join(path, file)) and compiled_regex.match(file)
    ]

    if len(files) == 0:
        raise FileNotFoundError(f"It was not possible to find files with regex {regex}")

    return files


def get_conf_file(file_name: str) -> dict:
    current_dir = get_current_folder()
    path = join(current_dir, "../param", file_name)

    return yaml.safe_load(Path(path).read_text())


def get_current_folder():
    return os.path.abspath(os.path.dirname(__file__))
