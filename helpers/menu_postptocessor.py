import re
import pandas as pd


class MenuPostprocessor:
    def __init__(self, path):
        """
        Read a csv file with data extracted from Excel files
        :param path: path to the csv file
        """
        self.csv_menu = pd.read_csv(path)

    @staticmethod
    def _ingredients_from_food(self, food):
        """
        Extract ingredients from food description
        :param food: A string, value from the Food column
        :return: A list of ingredients (strings) or empty list
        "Салат "Папарать-Кветка"(Говядина,ветчина,помидоры,огурцы)" -> ["говядина", "ветчина", "помидоры", "огурцы"]
        "Капуста тушеная" -> []
        """
        re_ingr = re.compile(r'\(([^\)]+)\)')
        ingr = re_ingr.findall(food)
        if ingr:
            ingr_parts = ingr[0].split(',')
            ingr_parts = [p.strip().lower() for p in ingr_parts]
            return ingr_parts
        else:
            return []

    @staticmethod
    def _weight_to_number(self, weight):
        """
        Convert a value from Weight column into a number
        :param weight: String value, weight as indicated in the respective column
        :return: a number; "2кусочек" -> 2, "шт." -> 1, "150" -> 150, "бдыщь" -> 1
        """
        try:
            wlen = len(weight.strip())
        except AttributeError:
            # if weight is np.nan
            return None
        if 0 == wlen:
            return None
        weight = weight.replace(",", ".")
        re_num = re.compile(r'\d+\.?\d?')
        weight_strings = re_num.findall(weight)
        # if the string looks like "150/20", then return largest number
        if weight_strings:
            weight_num = [float(w) for w in weight_strings]
            return max(weight_num)
        else:  # "шт."
            return 1.0

    @staticmethod
    def _price_to_number(self, price):
        """
        Convert a price value into a number
        :param price: string that indicates price of an item in a menu; "1 руб 82 коп", "70 коп" and similar
        :return: a number; "1 руб 82 коп" -> 1.82, "70 коп" -> 0.7 or None value if the input is in unknown format
        """
        re_rub = re.compile(r'(\d+)\s*?руб.*', re.IGNORECASE)
        re_kop = re.compile(r'(\d+)\s*?коп.*', re.IGNORECASE)
        try:
            rub = re_rub.findall(price)
            kop = re_kop.findall(price)
        except TypeError:  # price is null
            return None
        try:
            rub_num = int(rub[0])
        except IndexError:
            rub_num = None
        try:
            kop_num = int(kop[0])
        except IndexError:
            kop_num = None
        if rub_num is not None and kop_num is not None:
            return rub_num + kop_num/100
        elif rub_num is not None:
            return rub_num
        elif kop_num is not None:
            return kop_num/100
        else:
            return None
