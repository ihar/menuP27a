import re


def price_to_number(price):
    """
    Convert a price value into a number
    :param price: string that indicates price of an item in a menu; "1 руб 82 коп", "70 коп" and similar
    :return: a number; "1 руб 82 коп" -> 1.82, "70 коп" -> 0.7 or None value if the input is in unknown format
    """
    re_rub = r'(\d+)\s*?руб.*'
    re_kop = r'(\d+)\s*?коп.*'
    return None
