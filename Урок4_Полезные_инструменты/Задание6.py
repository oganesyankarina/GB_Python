"""6. Реализовать два небольших скрипта:
а) итератор, генерирующий целые числа, начиная с указанного,
б) итератор, повторяющий элементы некоторого списка, определенного заранее.
Подсказка: использовать функцию count() и cycle() модуля itertools.
Обратите внимание, что создаваемый цикл не должен быть бесконечным. Необходимо предусмотреть условие его завершения.
Например, в первом задании выводим целые числа, начиная с 3, а при достижении числа 10 завершаем цикл.
Во втором также необходимо предусмотреть условие, при котором повторение элементов списка будет прекращено.
"""
from itertools import count, cycle


def my_iterator_1(num1, num2):
    result = []
    for el in count(num1):
        if el > num2:
            break
        else:
            result.append(el)
    return result


def my_iterator_2(list_, num):
    result = []
    i = 0
    for item in cycle(list_):
        if i > num:
            break
        result.append(item)
        i += 1
    return result


print(my_iterator_1(3, 10))
print(my_iterator_2([1, 2, 3], 10))
