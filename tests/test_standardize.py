from standardize import get_data_files


def test_loop_through_files_in_data_drop_area_directory():
    files = get_data_files()

    assert len(files) == 3
