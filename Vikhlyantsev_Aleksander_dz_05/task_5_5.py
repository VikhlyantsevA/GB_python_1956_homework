# Задание 5
'''
Представлен список чисел. Определить элементы списка, не имеющие повторений.
Сформировать из этих элементов список с сохранением порядка их следования в исходном списке, например:
src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
result = [23, 1, 3, 10, 4, 11]

Подсказка: напишите сначала решение «в лоб». Потом подумайте об оптимизации.
'''
import time

def get_uniq_numbers_ver1(src: list):
    """
    Определяет элементы списка, не имеющие повторений.
    @param src: Исходный список
    @return: Список, элементов не имеющих повторений
    """
    # Вариант "в лоб"
    return [el for el in src if src.count(el) == 1]

def get_uniq_numbers_ver2(src: list):
    """
    Определяет элементы списка, не имеющие повторений.
    @param src: Исходный список
    @return: Список, элементов не имеющих повторений
    """
    # Оптимизированный по скорости вариант
    no_reply_els = set()
    unique_els = set()
    for el in src:
        if el not in unique_els:
            no_reply_els.add(el)
        else:
            no_reply_els.discard(el)
        unique_els.add(el)
    return [el for el in src if el in no_reply_els]


src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]

for func_name in map(lambda x: f'get_uniq_numbers_ver{x}', range(1, 3)):
    func = locals().get(func_name)
    if func:
        start = time.time()
        print(func_name, f'\tExecution result: {func(src)}', f'\tExecution time: {time.time() - start}', sep='\n', end='\n\n')

print(get_uniq_numbers_ver1(src) == get_uniq_numbers_ver2(src))
