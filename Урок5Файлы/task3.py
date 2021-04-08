"""3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
Выполнить подсчет средней величины дохода сотрудников.
"""


f_obj = open('task3_file.txt', encoding='utf-8')

staff = [line.strip().split() for line in f_obj]
f_obj.close()

low_salary = 20000
person_low_salary = [person[0] for person in staff if float(person[1]) < low_salary]
print(f'Сотрудники с окладом менее {int(low_salary/1000)} тыс. руб.: {", ".join(person_low_salary)}')

salary = [float(person[1]) for person in staff]
print(f'Средняя величина дохода сотрудников: {sum(salary)/len(salary)/1000} тыс. руб.')
