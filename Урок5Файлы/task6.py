"""6. Необходимо создать (не программно) текстовый файл, где каждая строка описывает
учебный предмет и наличие лекционных, практических и лабораторных занятий по этому предмету и их количество.
Важно, чтобы для каждого предмета не обязательно были все типы занятий.
Сформировать словарь, содержащий название предмета и общее количество занятий по нему. Вывести словарь на экран.
Примеры строк файла:
Информатика: 100(л) 50(пр) 20(лаб).
Физика: 30(л) — 10(лаб)
Физкультура: — 30(пр) —

Пример словаря:
{“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}
"""


f_obj = open('task6_file.txt', encoding='utf-8')
timetable = [line.strip().split() for line in f_obj]
f_obj.close()
print(timetable)

for index, item in enumerate(timetable):
    for i in range(1, len(item)):
        try:
            timetable[index][i] = int("".join(filter(str.isdecimal, timetable[index][i])))
        except ValueError:
            timetable[index][i] = 0
print(timetable)

classes = dict(zip([class_name[0] for class_name in timetable], [sum(class_name[1:]) for class_name in timetable]))
print(classes)
