"""1. Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()),
который должен принимать данные (список списков) для формирования матрицы.
Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
Примеры матриц вы найдете в методичке.
Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов класса Matrix
(двух матриц). Результатом сложения должна быть новая матрица.
Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки первой матрицы складываем
с первым элементом первой строки второй матрицы и т.д."""

A = [[31, 22], [37, 43], [51, 86]]
B = [[3, 5, 32], [2, 4, 6], [-1, 64, -8]]
C = [['qwe', 1], [1, 2], [2, 3]]
D = [[3, 5], [8, 3], [7, 1]]


class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix
        self.matrix_size = set((len(self.matrix), len(row)) for row in self.matrix)

    def __str__(self):
        return str('\n'.join(['\t'.join([str(j) for j in i]) for i in self.matrix]))

    def __add__(self, other):
        try:
            if self.matrix_size != other.matrix_size:
                return f'Матрицы должны иметь одинаковый размер!'

            result = []
            for item in zip(self.matrix, other.matrix):
                result.append([sum([j, k]) for j, k in zip(*item)])
            return Matrix(result)
        except TypeError:
            return f'Матрицы должны содержать числа!'


if __name__ == '__main__':

    matrix_a = Matrix(A)
    matrix_b = Matrix(B)
    matrix_c = Matrix(C)
    matrix_d = Matrix(D)

    print(matrix_a)

    print(matrix_a + matrix_b)
    print(matrix_a + matrix_c)
    print(matrix_a + matrix_d)
