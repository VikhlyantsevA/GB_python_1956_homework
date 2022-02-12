## Задание 5
'''
*(вместо 4) Рядом со скриптом task_4_4.py, создать скрипт task_4_5.py с содержимым аналогичным task_4_4.py, но
переработанным так, чтобы новый скрипт теперь срабатывал, как CLI, прямо в консоли/терминале.

Например:
python task_4_5.py USD
75.18, 2020-09-05
'''

import sys

import requests
from decimal import Decimal

def currency_rates(code: str) -> Decimal:
    """возвращает курс валюты `code` по отношению к рублю"""
    url = 'http://www.cbr.ru/scripts/XML_daily.asp'
    resp = requests.get(url).text
    start_idx = resp.find(f'<CharCode>{code}</CharCode>')
    if start_idx == -1:
        return
    resp_tail = resp[start_idx: ]
    end_idx = resp_tail.find('</Valute>')
    valute_info = resp_tail[: end_idx]

    valute_dict = {}
    for field in ['Nominal', 'Value']:
        open_tag, close_tag = f'<{field}>', f'</{field}>'
        start_cut = valute_info.find(open_tag) + len(open_tag)
        stop_cut = valute_info.find(close_tag)
        value = valute_info[start_cut: stop_cut].replace(',', '.')
        try:
            valute_dict[field] = Decimal(value)
        except:
            valute_dict[field] = value
    exchange_rate = valute_dict['Value'] / valute_dict['Nominal']
    return exchange_rate

def get_currency_rates(argv):
    program, *currencies = argv
    for currency in currencies:
        print(f'{currency}: {currency_rates(currency)}')

if __name__ == '__main__':
    sys.exit(get_currency_rates(sys.argv))
