import sys
import pandas as pd

from pathlib import Path


class MenuExtractor:
    def __init__(self, path):
        """
        Read an Excel file given its path
        :param path: an object of the Path class
        """
        self.path = path
        self._excel_data = None
        self._menu_keys = []
        try:
            self._excel_data = pd.read_excel(str(self.path), sheet_name=None)
        except FileNotFoundError as err:
            raise err
        # self._excel_data is an OrderedDict
        self._menu_keys = list(self._excel_data.keys())

    @property
    def excel_menus(self):
        return self._excel_data

    @property
    def menu_keys(self):
        return list(self._menu_keys)
