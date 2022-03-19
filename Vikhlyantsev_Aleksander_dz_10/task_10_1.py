# Задание 1
'''
Реализовать класс Matrix (матрица).
* Обеспечить перегрузку конструктора класса (метод __init__()), который должен
  принимать данные (список списков) для формирования матрицы. В случае если список списков некорректный -
  возбуждать исключение ValueError с сообщением `fail initialization matrix`.

Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.

Примеры матриц: 3 на 2, 3 на 3, 2 на 4.

| 31 43 |
| 22 51 |
| 37 86 |

| 3 5 32 |
| 2 4 6 |
| -1 64 -8 |

| 3 5 8 3 |
| 8 3 7 1 |

* Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде (как показано выше).
* Далее реализовать перегрузку метода __add__() для сложения двух объектов класса Matrix (двух матриц).
  Результатом сложения должна быть новая матрица.

> Подсказка: сложение элементов матриц выполнять поэлементно.
> Первый элемент первой строки первой матрицы складываем с первым элементом первой строки второй матрицы и пр.
'''
from typing import List


class Matrix:
    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix
        self.check_matrix()
        self.shape = (len(self.matrix), len(self.matrix[0]))

    def check_matrix(self):
        try:
            rows_lengths = list(set(map(len, self.matrix)))
            if len(rows_lengths) > 1:
                raise ValueError("fail initialization matrix")
            elif not rows_lengths[0]:
                raise ValueError("matrix can't be empty")
        except IndexError:
            raise ValueError('matrix must be of List[List[int]] type')

    def __str__(self) -> str:
        return '\n'.join([f'| {*line,} |' for line in self.matrix])

    def __add__(self, other):
        l_matrix = self.matrix
        r_matrix = other.matrix
        if self.shape != other.shape:
            raise Exception('Left and right matrixes must have same shape')
        values = [[l_matrix[i][j] + r_matrix[i][j] for j in range(self.shape[1])] for i in range(self.shape[0])]
        return Matrix(values)


if __name__ == '__main__':
    first_matrix = Matrix([[1, 2], [3, 4], [5, 6]])
    second_matrix = Matrix([[6, 5], [4, 3], [2, 1]])
    print(first_matrix, end='\n\n')
    """
    | 1 2 |
    | 3 4 |
    | 5 6 |
    """
    print(first_matrix + second_matrix, end='\n\n')
    """
    | 7 7 |
    | 7 7 |
    | 7 7 |
    """
    fail_matrix = Matrix([[1, 2], [3, 4, 7], [5, 6]])
    """
    Traceback (most recent call last):
      ...
    ValueError: fail initialization matrix
    """
    # fail_matrix_2 = Matrix([[], [], []])
    # fail_matrix_3 = Matrix([])
