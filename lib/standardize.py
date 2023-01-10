import os
import re
from os import listdir
from os.path import isfile, join
from pathlib import Path
from types import NoneType

import yaml


def get_data_files(regex: str = "") -> list[str]:
    compiled_regex = re.compile(regex)

    current_dir = os.path.abspath(os.path.dirname(__file__))
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
    current_dir = os.path.abspath(os.path.dirname(__file__))
    path = join(current_dir, "../param", file_name)

    return yaml.safe_load(Path(path).read_text())
