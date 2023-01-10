import os
import re
from os import listdir
from os.path import isfile, join


def get_data_files(regex: str = "") -> list[str]:
    compiled_regex = re.compile(regex)

    this_dir = os.getcwd()
    path = join(this_dir, "../dataDropArea")

    return [
        file
        for file in listdir(path)
        if isfile(join(path, file)) and compiled_regex.match(file)
    ]
