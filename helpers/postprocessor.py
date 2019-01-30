import re


def price_to_number(price):
    """
    Convert a price value into a number
    :param price: string that indicates price of an item in a menu; "1 руб 82 коп", "70 коп" and similar
    :return: a number; "1 руб 82 коп" -> 1.82, "70 коп" -> 0.7 or None value if the input is in unknown format
    """
    re_rub = re.compile(r'(\d+)\s*?руб.*', re.IGNORECASE)
    re_kop = re.compile(r'(\d+)\s*?коп.*', re.IGNORECASE)
    rub = re_rub.findall(price)
    kop = re_kop.findall(price)
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
