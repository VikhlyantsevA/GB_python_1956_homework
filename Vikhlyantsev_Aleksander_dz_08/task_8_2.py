# Задание 2
'''
Написать регулярное выражение для парсинга файла логов web-сервера из ДЗ 6 урока
[`nginx_logs.txt`](https://github.com/elastic/examples/raw/master/Common%20Data%20Formats/nginx_logs/nginx_logs)
 для получения информации вида:
`(<remote_addr>, <request_datetime>, <request_type>, <requested_resource>, <response_code>, <response_size>)`

Например:
raw = '188.138.60.101 - - [17/May/2015:08:05:49 +0000] "GET /downloads/product_2 HTTP/1.1" 304 0 "-" "Debian APT-HTTP/1.3 (0.9.7.9)"'
parsed_raw = ('188.138.60.101', '17/May/2015:08:05:49 +0000', 'GET', '/downloads/product_2', '304', '0')

> Примечание: вы ограничились одной строкой или проверили на всех записях лога в файле? Были ли особенные строки?
> Можно ли для них уточнить регулярное выражение?
'''
import re
from pprint import pprint


def get_parse_attrs(line: str) -> tuple:
    """
    Парсит строку на атрибуты и возвращает кортеж атрибутов:
    (<remote_addr>, <request_datetime>, <request_type>, <requested_resource>, <response_code>, <response_size>)
    """
    line_pattern = re.compile(r'''(?P<remote_addr>(?:\d{,3}\.?){4}|(?:[a-z\d]{,4}:?){8})
                                  \s*-\s*-\s*
                                  \[(?P<request_datetime>\d{2}/[A-Za-z]+/\d{4}(?::\d{2}){3}\s+\+\d{4})]
                                  \s+
                                  (?P<quotes>["])
                                        (?P<request_type>GET|HEAD)
                                        \s+
                                        (?P<requested_resource>(?=/)[/\w]+)
                                        \s+
                                        (?P<protocol>[\w/.]+)
                                  (?P=quotes)
                                  \s+
                                  (?P<response_code>\d{3})
                                  \s+
                                  (?P<response_size>\d+)
                                  \s+
                                  (?P=quotes)
                                        [\w/:.\-]+
                                  (?P=quotes)
                                  \s+
                                  (?P=quotes)
                                        (?P<os_info>.+)
                                  (?P=quotes)''', re.X | re.A)
    res = line_pattern.match(line)
    try:
        remote_addr = res.group('remote_addr')
        request_datetime = res.group('request_datetime')
        request_type = res.group('request_type')
        requested_resource = res.group('requested_resource')
        response_code = res.group('response_code')
        response_size = res.group('response_size')
        return remote_addr, request_datetime, request_type, requested_resource, response_code, response_size
    except AttributeError as ex:
        msg = f"Line doesn't fit pattern.Line is:\n{line}"
        raise ValueError(msg)


with open('nginx_logs.txt', 'r', encoding='utf-8') as fr:
    list_out = [get_parse_attrs(line.strip()) for line in fr]

pprint(list_out)
