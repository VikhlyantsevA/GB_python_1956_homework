# Задание 3
'''
Написать декоратор для логирования типов позиционных аргументов функции, например:
def type_logger...
    ...

@type_logger
def calc_cube(x):
   return x ** 3

$ a = calc_cube(5)
5: <class 'int'>

> Примечание: если аргументов несколько - выводить данные о каждом через запятую; можете ли вы вывести тип
> значения функции? Сможете ли решить задачу для именованных аргументов? Сможете ли вы замаскировать работу декоратора?
> Сможете ли вывести имя функции, например, в виде:

$ a = calc_cube(5)
calc_cube(5: <class 'int'>)
'''

from functools import wraps


def type_logger(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        varargs = [f'{arg}: {type(arg)}' for arg in args]
        keywords = [f'{k}={v}: {type(v)}' for k, v in kwargs.items()]
        arguments = varargs + keywords
        print(f'{func.__name__}({", ".join(arguments)})')
        res = func(*args, **kwargs)
        print()
        return res
    return wrapper


@type_logger
def calc_pow(x, n=2, **kwargs) -> list:
    "Возвращает список возведенных в степень n значений, переданных в функцию. По-умолчанию"
    say_hello = kwargs.get('say_hello')
    if say_hello:
        print('Hello, my friend. There was a test kwarg.')
    return x ** n


res = calc_pow(5, say_hello=True)

res = calc_pow(5, 3)

res = calc_pow(5, n=3)

print(calc_pow.__doc__)

