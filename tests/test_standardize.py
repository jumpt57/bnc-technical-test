import pytest

from standardize import get_data_files, get_conf_file


def test_loop_through_files_in_data_drop_area_directory_without_regex():
    files = get_data_files()
    assert len(files) == 6


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
