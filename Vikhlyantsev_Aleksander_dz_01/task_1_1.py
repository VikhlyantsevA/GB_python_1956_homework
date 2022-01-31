# Задание 1
'''
Реализовать вывод информации о промежутке времени в зависимости от его продолжительности `duration` в секундах:
# до минуты: <s> сек;
# до часа: <m> мин <s> сек;
# до суток: <h> час <m> мин <s> сек;
# в остальных случаях: <d> дн <h> час <m> мин <s> сек.

Примеры:
> duration = 53
53 сек

> duration = 153
2 мин 33 сек

> duration = 4153
1 час 9 мин 13 сек

> duration = 400153
4 дн 15 час 9 мин 13 сек

Примечание:
- можете проверить себя [здесь](https://www.epochconverter.com/);
- подумайте, можно ли использовать цикл для проверки работы кода сразу для нескольких значений продолжительности,
будет ли тут полезен список?
'''


def convert_time(duration: int) -> str:
    minutes, seconds = divmod(duration, 60)
    hours, minutes = divmod(minutes, 60)
    days, hours = divmod(hours, 24)

    if days == 0:
        if hours == 0:
            if minutes == 0:
                return f'{duration} сек'
            return f'{minutes} мин {seconds} сек'
        return f'{hours} час {minutes} мин {seconds} сек'
    return f'{days} дн {hours} час {minutes} мин {seconds} сек'


duration = 400153
result = convert_time(duration)
print(result)

duration = 66
result = convert_time(duration)
print(result)

duration = 59
result = convert_time(duration)
print(result)

print('\n')

durations = [400153, 66, 59]
results = [convert_time(duration) for duration in durations]
print(*results, sep='\n')
