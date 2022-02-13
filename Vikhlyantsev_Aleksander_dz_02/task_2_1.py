'''
Задание 1
Выяснить тип результата выражений:

15 * 3
15 / 3
15 // 2
15 ** 2
'''

def get_type(*args):
    for x in args:
        print(f'{x} type is {type(x)}')

get_type(15 * 3, 15 / 3, 15 // 2, 15 ** 2)