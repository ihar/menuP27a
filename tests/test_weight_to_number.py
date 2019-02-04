import pytest

from helpers.postprocessor import weight_to_number


@pytest.mark.parametrize("weight_string,weight_number", [
    ("", None),
    ("бдыщь!", 1.0),
    ("шт.", 1.0),
    ("2 кусочка", 2.0),
    ("2кусочек", 2.0),
    ("150/20", 150.0),
    ("20/150", 150),
    ("0,2", 0.2),
    ("0.2", 0.2),
])
def test_price2num_conversion(weight_string, weight_number):
    assert weight_to_number(weight_string) == weight_number
