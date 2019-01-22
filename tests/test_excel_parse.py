import pytest
from pathlib import Path
import datetime

from helpers.menu_extractor import MenuExtractor


@pytest.mark.parametrize("file_path,menus_num", [
    ("data/Меню с 02.04 по 06.04.2018г.xls", 5),
    ("data/Меню с 7-11 май.xls", 4),
    ("data/Меню с 08-11  января.xls", 4),
    ("data/Меню с 29.01 по 02.02.2018г.xls", 5),
])
def test_read_all_tabs(file_path, menus_num):
    mex = MenuExtractor(Path(file_path))
    assert len(mex.excel_menus) == menus_num


# menu_keys is a list of tab names of an Excel file;
# usually, that names are dates in string format
@pytest.mark.parametrize("file_path,menu_keys", [
    ("data/Меню с 02.04 по 06.04.2018г.xls",
     ['02.04.2018', '03.04.2018', '04.04.2018', '05.04.2018', '06.04.2018']),
    ("data/Меню с 7-11 май.xls", ['07.05.2018', '08.05.2018', '10.05.2018', '11.05.2018']),
])
def test_get_menu_keys(file_path, menu_keys):
    mex = MenuExtractor(Path(file_path))
    assert mex.menu_keys == menu_keys


# menu_keys is a list of tab names of an Excel file;
# usually, that names are dates in string format
@pytest.mark.parametrize("file_path,menu_dates", [
    ("data/Меню с 02.04 по 06.04.2018г.xls",
        [datetime.date(2018, 4, 2), datetime.date(2018, 4, 3), datetime.date(2018, 4, 4),
         datetime.date(2018, 4, 5), datetime.date(2018, 3, 30)]),  # the last one is unexpected, by the way
    ("data/Меню с 7-11 май.xls",
     [datetime.date(2018, 5, 7), datetime.date(2018, 5, 8),
      datetime.date(2018, 5, 10), datetime.date(2018, 5, 11)]),
])
def test_get_menu_dates(file_path, menu_dates):
    mex = MenuExtractor(Path(file_path))
    assert mex.menu_dates == menu_dates