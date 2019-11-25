import pytest
from helpers.yandex_speller import YandexSpeller


def test_correct_word():
    speller = YandexSpeller()
    suggestions = [response['s'][0] for response in speller.spell('корова')]
    assert 0 == len(suggestions)


def test_incorrect_word():
    speller = YandexSpeller()
    suggestions = [response['s'][0] for response in speller.spell('карова')]
    assert 1 == len(suggestions) and 'корова' == suggestions[0]

