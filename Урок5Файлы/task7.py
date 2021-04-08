"""7. Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме:
название, форма собственности, выручка, издержки.
Пример строки файла: firm_1 ООО 10000 5000.
Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
Если фирма получила убытки, в расчет средней прибыли ее не включать.
Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
Итоговый список сохранить в виде json-объекта в соответствующий файл.
Пример json-объекта:
[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]

Подсказка: использовать менеджеры контекста."""
from json import dump

f_obj = open('task7_file.txt', encoding='utf-8')
firms = [line.strip().split() for line in f_obj]
f_obj.close()

for item in firms:
    item.append(int(item[2]) - int(item[3]))

profits = [item[4] for item in firms if item[4] > 0]
print(f'Прибыль безубыточных компаний: {profits}')
print(f'Средняя прибыль безубыточных компаний: {sum(profits)/len(profits)}')

results = [dict(zip([item[0] for item in firms], [item[4] for item in firms])),
           {'average_profit': sum(profits)/len(profits)}]
print(results)

with open('task7_result_file.json', 'w', encoding='utf-8') as write_f:
    dump(results, write_f)

