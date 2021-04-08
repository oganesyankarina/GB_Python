# 5. Запросите у пользователя значения выручки и издержек фирмы.
# Определите, с каким финансовым результатом работает фирма
# (прибыль — выручка больше издержек, или убыток — издержки больше выручки).
# Выведите соответствующее сообщение.
# Если фирма отработала с прибылью, вычислите рентабельность выручки (соотношение прибыли к выручке).
# Далее запросите численность сотрудников фирмы и определите прибыль фирмы в расчете на одного сотрудника.


proceeds = int(input('Введите сумму выручки: '))
costs = int(input('Введите сумму издержек: '))

if proceeds >= costs:
    profit = True
    print(f'Финансовый результат положительный - получена прибыль в размере {proceeds - costs}')
else:
    profit = False
    print(f'Финансовый результат отрицательный - получен убыток в размере {proceeds - costs}')

if profit:
    print(f'Рентабельность выручки {round((proceeds - costs)/proceeds, 2)}')
    employees = int(input('Введите численность сотрудников: '))
    print(f'Прибыль на одного сотрудника {round((proceeds - costs) / employees, 2)}')
