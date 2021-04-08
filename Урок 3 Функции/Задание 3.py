# 3. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
# и возвращает сумму наибольших двух аргументов.


def func_sum_max_element(num1, num2, num3):
    try:
        return sum(sorted([num1, num2, num3])[-2:])
    except TypeError:
        return 'Введены некорректные значения (невозможно отсортировать и/или просуммировать)'


print(func_sum_max_element(1, 5, 2))
