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
