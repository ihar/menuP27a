import sys
import pandas as pd
import re
from datetime import datetime

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
        self._menu_dates = []
        try:
            self._excel_data = pd.read_excel(str(self.path), sheet_name=None)
            # The menu's title is in the header: self._excel_data.columns[0]
        except FileNotFoundError as err:
            raise err
        # self._excel_data is an OrderedDict
        self._menu_keys = list(self._excel_data.keys())
        self._menu_dates = self._extract_menu_dates()

    def _preprocess_menu(self, df_menu):
        """
        Drop NA columns that exist because menus in Excel files contain merged cells.
        The merged cells cause extra columns in pandas data frames having NA values.
        Those columns' names look like "Unnamed: 1"
        :param df_menu: pandas data frame as result of the pd.read_excel function
        :return: pandas data frame without NA columns and values of the mereged cells moved
        to additional column's value
        """
        df_menu_processed = df_menu.dropna(axis=1, how='all')
        # In case there is empty rows
        df_menu_processed = df_menu_processed.dropna(axis=0, how='all')

    def _extract_menu_dates(self):
        menu_dates = []
        for menu_df in self._excel_data.values():
            menu_title = menu_df.columns[0]
            date_str = re.findall(r"\d{2}\.\d{2}\.\d{4}", menu_title)
            try:
                date_date = datetime.strptime(date_str[0], "%d.%m.%Y").date()
            except (TypeError, ValueError):
                date_date = ''
            menu_dates.append(date_date)
        return menu_dates

    @property
    def excel_menus(self):
        return self._excel_data

    @property
    def menu_keys(self):
        return list(self._menu_keys)

    @property
    def menu_dates(self):
        return self._menu_dates
