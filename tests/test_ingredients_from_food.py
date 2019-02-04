import pytest

from helpers.postprocessor import ingredients_from_food


@pytest.mark.parametrize("food_string,ingredients", [
    ("", []),
    ("Суп-пюре из птицы", []),
    ("Ромштекс(говядина)", ["говядина"]),
    ("Солянка домашняя(картофель,огурцы,говядина,ветчина,лук,том.паста)",
     ["картофель", "огурцы", "говядина", "ветчина", "лук", "том.паста"]),
    ('Шницель "Нептун"(филе хека,  яйцо,  хлеб пшеничный)',
     ["филе хека", "яйцо", "хлеб пшеничный"]),
    ('Шницель "Нептун"(Филе хека,  Яйцо,  хлеб пшеничный)',
     ["филе хека", "яйцо", "хлеб пшеничный"]),
])
def test_price2num_conversion(food_string, ingredients):
    assert set(ingredients_from_food(food_string)) == set(ingredients)
