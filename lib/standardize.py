#!/usr/bin/python
import csv
import logging
import os
import re
from os import listdir
from os.path import isfile, join, abspath
from pathlib import Path
from types import NoneType
import click

import pandas
import yaml


class ParserError(pandas.errors.ParserError):
    pass


@click.command()
@click.option("--p", "param", prompt="The configuration file", default="config.yaml")
@click.option(
    "--d", "dump", prompt="Dump to files or print in terminal ?", default=False
)
def standardize(param: str, dump: bool):
    for file in traverse_and_format(param, dump):
        click.echo(file)


def traverse_and_format(config_file_name: str, dump_to_file: bool = False) -> list[str]:
    config = get_conf_file(config_file_name)

    def process_csv(pattern: str) -> list[str]:
        delimiter = config[pattern]["delimiter"]
        file_names = get_data_files(pattern)

        try:
            return [
                format_csv(file_name, delimiter, dump_to_file)
                for file_name in file_names
            ]
        except ValueError as e:
            logging.warning(str(e))
            return []

    out = []
    for file_name_pattern in config:
        for process_output in process_csv(file_name_pattern):
            out.append(process_output)

    return out


def format_csv(input_file_name: str, delimiter: str, dump_to_file: bool = False) -> str:
    with open(input_file_name, "r") as f:

        try:
            data_frame = pandas.read_csv(f, sep=delimiter)
        except pandas.errors.ParserError as e:
            raise ParserError(
                f"Error occurred for file {input_file_name} caused by {str(e)}"
            )

        logging.info("dump_to_file", dump_to_file)

        if dump_to_file:
            output_file_name = f"{input_file_name.split('.csv')[0]}_standardize.csv"
            data_frame.to_csv(
                output_file_name,
                sep=",",
                quotechar="'",
                quoting=csv.QUOTE_NONNUMERIC,
                index=False,
            )
            return f"CSV file was dumped has {output_file_name}"
        else:
            return data_frame.to_csv(
                None, sep=",", quotechar="'", quoting=csv.QUOTE_NONNUMERIC, index=False
            )


def get_data_files(regex: str = "") -> list[str]:
    compiled_regex = re.compile(regex)

    current_dir = get_current_folder()
    path = join(current_dir, "../dataDropArea")

    files = [
        abspath(join(path, file))
        for file in listdir(path)
        if isfile(join(path, file)) and compiled_regex.match(file)
    ]

    files.sort()

    if files is None or files is NoneType or len(files) == 0:
        raise FileNotFoundError(f"It was not possible to find files with regex {regex}")

    return files


def get_conf_file(file_name: str) -> dict:
    current_dir = get_current_folder()
    path = abspath(join(current_dir, "../param", file_name))

    return yaml.safe_load(Path(path).read_text())


def get_current_folder():
    return os.path.abspath(os.path.dirname(__file__))


if __name__ == "__main__":
    standardize()
