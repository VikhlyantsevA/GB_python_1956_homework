# Задание 3
'''
Реализовать склонение слова `процент` во фразе `N процентов`.
Вывести эту фразу на экран отдельной строкой для каждого из чисел в интервале `от 1 до 100`:

1 процент
2 процента
3 процента
4 процента
5 процентов
6 процентов
...
100 процентов
'''


def transform_string(number: int) -> str:
    """Возвращает строку вида 'N процентов' с учётом склонения по указанному number"""
    list_1 = list(range(1, 101, 10))
    list_1.remove(11)

    list_2 = sorted([x for num in range(2, 5) for x in range(num, 101, 10) if x not in range(12, 15)])

    if number in list_1:
        suffix = ''
    elif number in list_2:
        suffix = 'а'
    else:
        suffix = 'ов'
    return f'{number} процент{suffix}'


for n in range(1, 101):
    print(transform_string(n))