import pytest

from helpers.postprocessor import price_to_number


@pytest.mark.parametrize("price_string,price_number", [
    ("", None),
    ("10$", None),
    ("$10.5", None),
    ("10", None),
    ("86 коп", 0.86),
    ("86 Коп", 0.86),
    ("86коп", 0.86),
    ("2 руб 04 коп", 2.04),
    ("2 руб 4 коп", 2.04),
    ("1 руб", 1),
    ("1 РУБ.", 1),
    ("1 руб 18 коп", 1.18),
    ("1 руб18 коп", 1.18),
    ("1 руб 18коп", 1.18),
    ("4     руб     03    коп    ", 4.03),
])
def test_price2num_conversion(price_string, price_number):
    assert price_to_number(price_string) == price_number
