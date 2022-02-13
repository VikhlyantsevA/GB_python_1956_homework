# Задание 2
'''
На вход будет выдаваться список, пример:
['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']

a) Необходимо его обработать — обособить каждое целое число (вещественные не трогаем) кавычками
(добавить кавычку до и кавычку после элемента списка, являющегося числом) и дополнить нулём
до двух целочисленных разрядов:

['в', '"', '05', '"', 'часов', '"', '17', '"', 'минут', 'температура', 'воздуха', 'была', '"', '+05', '"', 'градусов']
'''

def convert_list_in_str(list_in: list) -> str:
    """Обособляет каждое целое число кавычками, добавляя кавычку до и после элемента
        списка, являющегося числом, и дополняет нулём до двух целочисленных разрядов.
        Формирует из списка результирующую строковую переменную и возвращает."""
    list_out = []
    for el in list_in:
        stripped_el = el.lstrip('-+ ')
        if stripped_el.isdigit():
            formated_el = el.replace(stripped_el, f'{int(stripped_el):02d}')
            list_out += ['"', formated_el, '"']
        else:
            list_out.append(el)
    return list_out


my_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
result = convert_list_in_str(my_list)
print(result)

'''
b) Сформировать из обработанного списка строку:
`в "05" часов "17" минут температура воздуха была "+05" градусов`
'''
def split_list_by_idxs(list_: list, idxs: list) -> list:
    '''
    Разбивает список на список со вложенными списками по индексам
    :param list_: Исходный список формата list[str]
    :param idxs: Список индексов, по которым разбивается list_
    '''
    return [list_[start: end] for start, end in zip([0] + idxs, idxs + [len(list_)])]

quotes_idx = [i for i, el in enumerate(result) if el == '"']

# Включаем вторые кавычки в срез по индексам
idxs_to_slice = [idx + 1 if i % 2 == 0 else idx for i, idx in enumerate(quotes_idx, start=1)]
splitted_list = split_list_by_idxs(result, idxs_to_slice)

print(' '.join([' '.join(sub_list).replace('" ', '"').replace(' "', '"') for sub_list in splitted_list]))

