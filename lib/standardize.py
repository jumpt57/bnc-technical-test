import os
import re
from os import listdir
from os.path import isfile, join


def get_data_files(regex: str = "") -> list[str]:
    compiled_regex = re.compile(regex)

    current_dir = os.path.abspath(os.path.dirname(__file__))
    path = join(current_dir, "../dataDropArea")

    return [
        file
        for file in listdir(path)
        if isfile(join(path, file)) and compiled_regex.match(file)
    ]
