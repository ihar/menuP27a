import pytest
from pathlib import Path

from helpers.menu_extractor import MenuExtractor


def test_read_nonexisting_files():
    with pytest.raises(FileNotFoundError):
        mex = MenuExtractor(Path('data/is_wrong/I do not exist.xlsx'))


def test_read_existing_files():
    try:
        mex = MenuExtractor(Path('data/Меню с 02.04 по 06.04.2018г.xls'))
    except FileNotFoundError:
        pytest.fail("Unexpected FileNotFound error.")


@pytest.mark.parametrize("file_path,menus_num", [
    ("data/Меню с 02.04 по 06.04.2018г.xls", 5),
    ("data/Меню с 7-11 май.xls", 4),
    ("data/Меню с 08-11  января.xls", 4),
    ("data/Меню с 29.01 по 02.02.2018г.xls", 5),
])
def test_read_all_tabs(file_path, menus_num):
    mex = MenuExtractor(Path(file_path))
    assert len(mex.excel_menus) == menus_num

