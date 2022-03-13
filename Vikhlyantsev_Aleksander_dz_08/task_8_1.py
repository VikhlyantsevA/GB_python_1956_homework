# Задание 1
'''
Написать тело функцию email_parse(email: str), которая при помощи регулярного выражения извлекает имя
пользователя и почтовый домен из email адреса и возвращает их в виде словаря.
Если адрес не валиден, выбросить исключение ValueError.

Пример:
$ email_parse('someone@geekbrains.ru')
{'username': 'someone', 'domain': 'geekbrains.ru'}

$ email_parse('someone@geekbrainsru')
Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
    ...
        raise ValueError(msg)
ValueError: wrong email: someone@geekbrainsru
'''
import re


def email_parse(email: str) -> dict:
    """
    Парсит переданную email-строку на атрибуты и возвращает словарь
    :param email: строковое входное значение обрабатываемого email
    :return: {'username': <значение до символа @>, 'domain': <значение за символом @>} | ValueError
    """
    RE_MAIL = re.compile(r'(?P<username>[\w\-.]+)@(?P<domain>(?:(?!-)(?!.*--)[\w\-]{,63}(?<!-)\.)+[a-z]+)',
                         flags=re.A | re.I)
    res = RE_MAIL.match(email)
    try:
        return {'username': res.group('username'), 'domain': res.group('domain')}
    except AttributeError:
        msg = f'Wrong email: {email}'
        raise ValueError(msg)


if __name__ == '__main__':
    print(email_parse('someone@geekbrains.ru'))
    print(email_parse('someone@geekbrainsru'))
