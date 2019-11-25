import requests


class YandexSpeller:
    """
    Implementation of Yandex's speller: https://yandex.ru/dev/speller/
    This is a simple version that does not support all available options.
    """
    def __init__(self):
        self._lang = 'ru'
        self._api_query = 'https://speller.yandex.net/services/spellservice.json/checkText'

    def _spell_text(self, text):
        data = {
            'text': text,
            'lang': self._lang,
        }
        response = requests.post(url=self._api_query, data=data).json()
        return response

    def spell(self, text):
        for item in self._spell_text(text):
            yield item


