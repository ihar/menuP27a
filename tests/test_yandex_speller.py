import pytest
from helpers.yandex_speller import YandexSpeller


@pytest.mark.parametrize("word",
                         ["салат", "Салат", "пудинг", "чесночной", "бендерики", "капрезе"])
def test_correct_word(word):
    speller = YandexSpeller()
    suggestions = [response['s'][0] for response in speller.spell(word)]
    assert 0 == len(suggestions)


@pytest.mark.parametrize("word,correct_word",
                         [("салад", "салат"), ("пуддинг", "пудинг"),
                          ("тушенная", "тушеная"), ("пшеная", "пшенная"),
                          ("пшонная", "пшенная"), ("пшрнная", "пшенная")])
def test_incorrect_word(word, correct_word):
    speller = YandexSpeller()
    suggestions = [response['s'][0] for response in speller.spell(word)]
    assert 1 == len(suggestions) and correct_word == suggestions[0]

