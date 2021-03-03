# 3. Узнайте у пользователя число n.
# Найдите сумму чисел n + nn + nnn.
# Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.


def input_n():
    str_n = input('Введите число: ')
    if str_n.isdigit():
        n = int(str_n)
        nn = int(str_n + str_n)
        nnn = int(str_n + str_n + str_n)
        print(f'{n} + {nn} + {nnn} = {sum([n, nn, nnn])}')
    else:
        print('Вы ввели символы!')
        input_n()


input_n()
