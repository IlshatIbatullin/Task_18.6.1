# import pyTelegramBotAPI
import requests
import json
from config import keys


class APIException(Exception):  # исключения для отлавливания
    pass


class CurrencyConverter:  # конвертер валюты
    @staticmethod
    def get_price(quote: str, base: str, amount: str):
        if quote == base:  # перевод, например, доллара в доллар
            raise APIException(f'Невозможно перевести одинаковые валюты {base}.')

        try:
            quote_ticker = keys[quote]
        except KeyError:
            raise APIException(f'Не удалось обработать валюту {quote}')

        try:
            base_ticker = keys[base]
        except KeyError:
            raise APIException(f'Не удалось обработать валюту {base}')
        try:
            amount = float(amount)  # amount количество не строка, а вещественное
        except ValueError:
            raise APIException(f'Не удалось обработать количество {amount}')

        r = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym={quote_ticker}&tsyms={base_ticker}')
        total_base = json.loads(r.content)[keys[base]] * amount

        return total_base










