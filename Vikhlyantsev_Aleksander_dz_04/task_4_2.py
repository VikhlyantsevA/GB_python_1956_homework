## Задание 2
'''В корневой директории урока создать task_4_2.py и написать в нём функцию currency_rates(),
принимающую в качестве аргумента код валюты (например, USD, EUR, SGD, ...) и
возвращающую курс этой валюты по отношению к рублю.

Использовать библиотеку requests.

В качестве API можно использовать http://www.cbr.ru/scripts/XML_daily.asp.

Рекомендация: выполнить предварительно запрос к API в обычном браузере, посмотреть содержимое ответа.

* Можно ли, используя только методы класса str, решить поставленную задачу?
* Функция должна возвращать результат числового типа, например float.

Подумайте:
* есть ли смысл для работы с денежными величинами использовать вместо float тип Decimal?
* Сильно ли усложняется код функции при этом?

Если в качестве аргумента передали код валюты, которого нет в ответе, вернуть `None`.

Можно ли сделать работу функции не зависящей от того, в каком регистре был передан аргумент?
В качестве примера выведите курсы доллара и евро.
'''

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


print(currency_rates("USD"))
print(currency_rates("noname"), end='\n\n')

# А вообще было бы удобнее использовать библиотеку xml или регулярные выражения для парсинга.
# Вариант выше только с использованием методов класса str как требовалось в задании, полагаю.
from xml.etree import ElementTree


def currency_rates_ver2(code: str) -> Decimal:
    """возвращает курс валюты `code` по отношению к рублю"""
    url = 'http://www.cbr.ru/scripts/XML_daily.asp'
    resp = ElementTree.fromstring(requests.get(url).content)

    # Спарсим данные в словари
    valute_info = [{field.tag: field.text for field in valute} for valute in resp]

    # Оформим valute_info в словарь для удобства поиска по коду валюты, например.
    valute_dict = {data.pop('CharCode'): data for data in valute_info}

    if code in valute_dict:
        value = Decimal(valute_dict.get(code).get('Value').replace(',', '.'))
        nominal = int(valute_dict.get(code).get('Nominal'))
        exchange_rate = value / nominal
        return exchange_rate

print(currency_rates_ver2("USD"))
print(currency_rates_ver2("noname"))