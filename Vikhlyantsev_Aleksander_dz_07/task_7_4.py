# Задание 4
'''
Написать скрипт, который выводит статистику для заданной папки в виде словаря, в котором ключи — верхняя граница
размера файла (пусть будет кратна 10), а значения — общее количество файлов (в том числе и в подпапках),
размер которых не превышает этой границы, но больше предыдущей (начинаем с 0), например:

{
  100: 15,
  1000: 3,
  10000: 7,
  100000: 2
}

Тут 15 файлов размером не более 100 байт; 3 файла больше 100 и не больше 1000 байт...

> Подсказка: размер файла можно получить из атрибута .st_size объекта os.stat.
'''
import os
import math
from pprint import pprint

def get_files_stats(path: str) -> dict:
    res = dict()
    for item in os.scandir(path):
        # Для удобства округлим до ближайшего целого числа
        file_size = math.ceil(item.stat().st_size)
        if file_size % 10 == 0:
            key = file_size
        else:
            range = len(str(file_size))
            key = 10 ** range
        res[key] = res.get(key, 0) + 1
    return res

if __name__ == '__main__':
    path = os.path.dirname(os.path.abspath(__file__))
    # Информация о содержимом папки
    print(path)
    print(*sorted([item.stat().st_size for item in os.scandir(path)]))
    # Результат
    pprint(get_files_stats(path), indent=2)
