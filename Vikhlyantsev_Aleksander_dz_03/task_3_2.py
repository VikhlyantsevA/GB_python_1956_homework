# Задание 2
'''
(вместо задачи 1) Перепишите функцию из задания 1 изменив название на `num_translate_adv()`:
реализовать корректную работу с числительными, начинающимися с заглавной буквы — результат тоже
должен быть с заглавной.

Например:
num_translate_adv("One")
"Один"

num_translate_adv("two")
"два"
'''
import string

def num_translate_adv(value: str) -> str:
    """переводит числительное с английского на русский с учетом регистра первого символа"""
    numbers_en_ru = {
        'zero': 'ноль',
        'one': 'один',
        'two': 'два',
        'three': 'три',
        'four': 'четыре',
        'five': 'пять',
        'six': 'шесть',
        'seven': 'семь',
        'eight': 'восемь',
        'nine': 'девять',
        'ten': 'десять'
    }

    str_out = numbers_en_ru.get(value.lower())
    return str_out.title() if value and value[0] in string.ascii_uppercase else str_out


print(num_translate_adv("One"))
print(num_translate_adv("eight"))
