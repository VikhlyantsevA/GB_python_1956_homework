# Задание 4
'''
Написать декоратор с аргументом-функцией (`callback`), позволяющий валидировать входные значения функции и выбрасывать
исключение `ValueError`, если что-то не так, например:
$ calc_cube(5)
125
$ calc_cube(-5)
Traceback (most recent call last):
  ...
    raise ValueError(msg)
ValueError: wrong val -5
```

Исключение должно возбуждаться, если значение анализируемого аргумента не является положительным целочисленным
значением, включая 0.

> Примечание: сможете ли вы замаскировать работу декоратора?
'''

import decimal
from functools import wraps
from decimal import Decimal

def callback(*args):
    for arg in args:
        if not isinstance(arg, (int, float, decimal.Decimal)) or arg <= 0:
            raise ValueError(f'Wrong value {arg}')


def val_checker(check_func=None):
    def func_decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            if check_func:
                check_func(*args)
            res = func(*args, **kwargs)
            return res
        return wrapper
    return func_decorator



@val_checker(callback)
def calc_cube(x):
    """Возведение числа в третью степень"""
    return x ** 3


if __name__ == '__main__':
    print(calc_cube(5))
    print(calc_cube(Decimal('2.5')))
    print(calc_cube(3.5))
    print(calc_cube(-10))
    print(calc_cube('ss'))

    print(calc_cube.__doc__)