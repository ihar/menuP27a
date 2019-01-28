from pathlib import Path

from helpers.menu_extractor import MenuExtractor

FILE_PATH = Path('data/Меню с 7-11 май.xls')

if __name__ == '__main__':
    mex = MenuExtractor(FILE_PATH)

    menu_keys = mex.menu_keys
    print(menu_keys)
    menus_list = mex.menus_list
    print(menu_keys[0])
    menu_day = menus_list[0]
    print(menu_day.shape)
    print(menu_day)

    print(mex.menus_combined.shape)

    print("Done.")
