"""5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
"""


while True:
    try:
        numbers = list(map(float, input('Введите числа через пробел: ').split()))

        f_obj = open('task5_file.txt', 'w', encoding='utf-8')
        f_obj.writelines('\n'.join(list(map(str, numbers))))
        f_obj.close()

        f_obj = open('task5_file.txt', encoding='utf-8')
        numbers = list(map(float, [line.strip() for line in f_obj]))
        f_obj.close()

        print(f'Числа из файла: {numbers}.\nСумма чисел в файле: {sum(numbers)}')
        break
    except ValueError:
        print('Некорректный ввод! Необходимо вводить числа через пробел.')
        continue
