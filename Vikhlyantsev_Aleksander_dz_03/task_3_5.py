# Задание 5
'''
Реализовать функцию get_jokes(), возвращающую n шуток, сформированных из трех случайных слов,
взятых из трёх списков (по одному из каждого):

nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]

Например:
get_jokes(2)
["лес завтра зеленый", "город вчера веселый"]

Документировать код функции.

* Сможете ли вы добавить еще один аргумент — флаг, разрешающий или запрещающий повторы слов в
шутках (когда каждое слово можно использовать только в одной шутке)?
* Сможете ли вы сделать аргументы именованными?
'''
import random

nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]

def get_jokes(count: int) -> list:
    """Возвращает список шуток в количестве count"""
    lists_ = [nouns, adverbs, adjectives]
    list_out = [' '.join([random.choice(list_) for list_ in lists_]) for i in range(count)]
    return list_out

print('Тест функции get_jokes.')
print(get_jokes(2))
print(get_jokes(10))
print()


# Раскомментируйте для реализации подзаданий: документирование, флаг и именованные аргументы
def get_jokes_adv(**kwargs) -> list:
    """
    Возвращает список шуток в количестве count
    :count: количество возвращаемых шуток
    :no_reply: флаг, разрешающий или запрещающий повторы слов в шутках (когда каждое слово можно использовать только в одной шутке)
    """
    jokes_num = kwargs.get('count', 1)
    no_reply = kwargs.get('no_reply', False)

    lists_ = [nouns, adverbs, adjectives]

    max_jokes_num = min([len(list_) for list_ in lists_])
    if no_reply:
        if jokes_num > max_jokes_num:
            raise Exception(f'Невозможно вывести {jokes_num} шуток. Выберите значение меньше {max_jokes_num} или уберите флаг \
no_reply, запрещающий повторное использование слов в разных шутках.')

        return list(map(' '.join, zip(*[random.sample(list_, jokes_num) for list_ in lists_])))
    return [' '.join([random.choice(list_) for list_ in lists_]) for i in range(jokes_num)]

print('Тест функции get_jokes_adv.')
print(get_jokes_adv(count=2))
print(get_jokes_adv(count=4, no_reply=True))

# Вызывает ошибку. Для теста можно раскомментировать.
# print(get_jokes_adv(count=10, no_reply=True))