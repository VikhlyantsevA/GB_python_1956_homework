# Задание 2
'''
a) Создать список, состоящий из кубов нечётных чисел от 1 до 1000.
Вычислить сумму тех чисел из этого списка, сумма цифр которых делится нацело на 7.

Например, число 19 ^ 3 = 6859 будем включать в сумму, так как 6 + 8 + 5 + 9 = 28 – делится нацело на 7.
Внимание: использовать только арифметические операции!

b) К каждому элементу списка добавить 17 и заново вычислить сумму тех чисел из этого списка, сумма цифр которых
  делится нацело на 7.

*c) Решить задачу под пунктом b, не создавая новый список. (если будете решать - либо создайте доп. функцию, либо
  перепишите существующую sum_list_2)
'''


# а)
# Вариант 1 (более компактный)
def sum_list_1_1(dataset: list) -> int:
    """Вычисляет сумму чисел списка dataset, сумма цифр которых делится нацело на 7"""
    return sum([num for num in dataset if sum(list(map(int, list(str(num))))) % 7 == 0])


# Вариант 2
def sum_list_1_2(dataset: list) -> int:
    """Вычисляет сумму чисел списка dataset, сумма цифр которых делится нацело на 7"""
    sum_numbers = 0
    for num in dataset:
        sum_digits = 0
        for digit in list(str(num)):
            sum_digits += int(digit)
        if sum_digits % 7 == 0:
            sum_numbers += num
    return sum_numbers


# б)
def sum_list_2_1(dataset: list) -> int:
    """К каждому элементу списка добавляет 17 и вычисляет сумму чисел списка,
        сумма цифр которых делится нацело на 7"""
    new_dataset = []
    for num in dataset:
        new_dataset.append(num + 17)
    return sum_list_1_2(new_dataset)


# в)
# Если я правильно понял задачу, то должно выглядеть как-то так
def sum_list_2_2(dataset: list) -> int:
    """К каждому элементу списка добавляет 17 и вычисляет сумму чисел списка,
        сумма цифр которых делится нацело на 7"""
    return sum_list_1_2([num + 17 for num in dataset])


my_list = [i ** 3 for i in range(1, 1001)]

result_1_1 = sum_list_1_1(my_list)
result_1_2 = sum_list_1_2(my_list)
print(result_1_1, result_1_2, sep='\n', end='\n\n')

result_2_1 = sum_list_2_1(my_list)
result_2_2 = sum_list_2_2(my_list)
print(result_2_1, result_2_2, sep='\n', end='\n\n')
