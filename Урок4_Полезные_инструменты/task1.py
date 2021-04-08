"""1. Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
В расчете необходимо использовать формулу: (выработка в часах * ставка в час) + премия.
Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.
"""
from sys import argv


def calculate_salary(working_out, wage_rate,  premium):
    try:
        return int(working_out) * int(wage_rate) + int(premium)
    except TypeError:
        return 'Некорректный ввод!'
    except ValueError:
        return 'Некорректный ввод!'


script_name, first_param, second_param, third_param = argv

print("Имя скрипта: ", script_name)
print("Параметр 1 - выработка в часах: ", first_param)
print("Параметр 2 - ставка в час: ", second_param)
print("Параметр 3 - премия: ", third_param)
print("Рассчитанная заработная плата сотрудника: ", calculate_salary(first_param, second_param, third_param))
