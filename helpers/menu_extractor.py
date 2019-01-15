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
        try:
            excel_data = pd.read_excel(str(self.path), sheet_name=None)
        except FileNotFoundError as err:
            raise err
