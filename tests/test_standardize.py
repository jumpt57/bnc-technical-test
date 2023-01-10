from standardize import get_data_files


def test_loop_through_files_in_data_drop_area_directory_without_regex():
    files = get_data_files()
    assert len(files) == 6


def test_loop_through_files_in_data_drop_area_directory_with_regex():
    files = get_data_files("file_test_1_[0-9]{8}.csv")
    assert len(files) == 3
