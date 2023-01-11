import re
import tempfile

import pytest

from standardize import (
    get_data_files,
    get_conf_file,
    format_csv,
    traverse_and_format,
    ParserError,
)


def test_loop_through_files_in_data_drop_area_directory_without_regex():
    files = get_data_files()

    assert len(files) == 6

    to_find = re.compile(".*/dataDropArea/file_test_1_20200101.csv")
    assert list(filter(to_find.match, files))


def test_loop_through_files_in_data_drop_area_directory_with_regex():
    files = get_data_files("file_test_1_[0-9]{8}.csv")
    assert len(files) == 3


def test_error_loop_through_files_in_data_drop_area_directory_with_regex():
    with pytest.raises(FileNotFoundError):
        get_data_files("test")


def test_read_conf_file():
    conf = get_conf_file("config.yaml")

    assert conf == {
        "file_test_1_[0-9]{8}.csv": {"delimiter": ",", "column_count": 5},
        "file_test_2_[0-9]{8}.csv": {"delimiter": ";", "column_count": 4},
        "file_test_3_[0-9]{8}.csv": {"delimiter": "|", "column_count": 4},
    }


def test_error_read_conf_file():
    with pytest.raises(FileNotFoundError):
        get_conf_file("test")


def test_format_csv():
    with tempfile.NamedTemporaryFile(mode="w+") as input_tmp:
        input_tmp.write("This,is,a,test,20200101")
        input_tmp.seek(0)

        formatted = format_csv(input_tmp.name, ",", 5)

        assert formatted == "'This','is','a','test','20200101'\n"


def test_error_format_csv():
    with pytest.raises(FileNotFoundError):
        format_csv("test", ",", 5)


def test_error_format_csv_columns():
    with pytest.raises(ParserError):
        with tempfile.NamedTemporaryFile(mode="w+") as input_tmp:
            input_tmp.write(
                """Another|test|file|date
            This|is|test|20200520
            This|is||est|20200520
            This|is|test|20200520
            This|is|test|20200520
            This|is|test|20200520
            This|is|te,t|20200520
            This|is|test|20200520
            This|is|test data again|20200520
            """
            )
            input_tmp.seek(0)

            format_csv(input_tmp.name, "|", 4)


def test_traverse_and_format():
    formatted_csv = traverse_and_format("config.yaml")

    assert len(formatted_csv) == 5
