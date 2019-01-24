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
        self._menu_dic = {}
        try:
            self._excel_data = pd.read_excel(str(self.path), sheet_name=None)
            # The menu's title is in the header: self._excel_data.columns[0]
        except FileNotFoundError as err:
            raise err
        # self._excel_data is an OrderedDict
        self._menu_keys = list(self._excel_data.keys())
        self._menu_dates = self._extract_menu_dates()
        # Preprocess each tab of the excel file and generate a dictionary
        # in the menu_key => menu_df dictionary
        self._menu_dic = \
            {menu_key: self._preprocess_menu(self._excel_data[menu_key]) for menu_key in self._menu_keys}

    @staticmethod
    def _preprocess_menu(df_menu):
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
        # In case there are random characters in NA columns, they might not be deleted
        # Left the first three columns only since all necessary info is in these columns
        df_menu_processed = df_menu_processed.iloc[:, :3]
        df_menu_processed.columns = ['Food', 'Weight', 'Price']
        # Rows with NA in the last column is the names of a section like
        # "Супы", "Гарниры", "Сладкие блюда" and so on.
        # Delete these rows and put the sections' names as values in the additional columns
        fourth_column_values = []
        current_type = ''
        for row in df_menu_processed.itertuples(index=True, name='Pandas'):
            if pd.isnull(row.Price):
                current_type = row.Food
            fourth_column_values.append(current_type)
        df_menu_processed['Type'] = fourth_column_values
        # Delete the rows with the sections' names:
        df_menu_processed = df_menu_processed.dropna(axis=0, subset=['Price'])
        return df_menu_processed

    def _extract_menu_dates(self):
        """
        Convert tab names which are in the dd.mm.yyyy format
        to a date object
        :return: A list of dates that correspond to the tab names
        """
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
        return self._menu_keys

    @property
    def menu_dates(self):
        return self._menu_dates

    @property
    def menu_data_dic(self):
        return self._menu_dic
