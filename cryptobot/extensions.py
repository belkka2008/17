import json
import requests
from config import keys
class ApiException(Exception):
    pass

class Cryptoconverter:
    @staticmethod
    def get_price(quote: str, base: str, amount: int):

        if quote == base:
            raise ApiException(f'Невозможно перевести одинаковые валюты {base}.')

        try:
            quote_ticker = keys[quote]
        except KeyError:
            raise ApiException(f'Не удалось обработать валюту {quote}.')


        try:
            base_ticker = keys[base]
        except KeyError:
            raise ApiException(f'Не удалось обработать валюту {base}.')

        try:
            amount = float(amount)
        except ValueErrorError:
            raise ApiException(f'Не удалось обработать количество {amount}.')

        r = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym={quote_ticker}&tsyms={base_ticker}')
        total_base = json.loads(r.content)[keys[base]]

        return total_base*amount
