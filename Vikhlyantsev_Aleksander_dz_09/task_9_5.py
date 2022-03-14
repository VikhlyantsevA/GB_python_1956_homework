# Задание 5
'''
Реализовать класс Stationery (канцелярская принадлежность):
* определить в нём атрибут title (название) и метод draw (отрисовка). Метод выводит сообщение Запуск отрисовки;
* создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер);
* реализовать переопределение метода draw таким образом, чтобы для каждого класса метод
  выводил в stdout только сообщение формата <Имя класса>: приступил к отрисовке объекта "<title>", при этом
  для класса Pencil при запуске метода draw в stdout сначала выводить сообщение Запуск отрисовки, а потом
  своё уникальное по формату;
* создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.
'''
from functools import wraps

class Stationery:

    def __init__(self, title: str) -> None:
        self.title = title

    def draw(self) -> None:
        print('Запуск отрисовки')




class Pen(Stationery):
    def draw(self) -> None:
        print(f'{self.__class__.__name__}: приступил к отрисовке объекта "{self.title}"')

class Pencil(Pen, Stationery):
    def draw(self) -> None:
        Stationery.draw(self)
        Pen.draw(self)

class Handle(Pen, Stationery): ...


if __name__ == '__main__':
    pen = Pen('Ручка')
    pencil = Pencil('Карандаш')
    handle = Handle('Маркер')
    pen.draw()  # Pen: приступил к отрисовке объекта "Ручка"
    handle.draw()  # Handle: приступил к отрисовке объекта "Маркер"
    pencil.draw()  # Пример вывода ниже в многострочном комментарии
    """
    Запуск отрисовки
    Pencil: приступил к отрисовке объекта "Карандаш"
    """
