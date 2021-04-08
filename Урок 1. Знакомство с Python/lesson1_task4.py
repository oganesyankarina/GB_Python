# 4. Пользователь вводит целое положительное число.
# Найдите самую большую цифру в числе.
# Для решения используйте цикл while и арифметические операции.


def input_n():
    n = input('Введите целое положительное число: ')
    if n.isdigit():
        n = list(n)
        max_element = n[0]
        i = 1
        while i < len(n):
            if n[i] > max_element:
                max_element = n[i]
            i += 1
        print(f'Самая большая цифра в числе: {max_element}')
    else:
        print('Вы ввели символы!')
        input_n()


input_n()
