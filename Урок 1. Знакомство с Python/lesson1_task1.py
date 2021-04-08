# 1. Поработайте с переменными, создайте несколько, выведите на экран,
# запросите у пользователя несколько чисел и строк и сохраните в переменные, выведите на экран.


def get_suff(some_string):
    if some_string[-1] in ['1']:
        suff = 'год'
    elif some_string[-1] in ['2', '3', '4']:
        suff = 'годa'
    else:
        suff = 'лет'
    return suff


first_name = 'Оганесян'
last_name = 'Карина'
age = 32
message = f'Привет! Меня зовут {first_name} {last_name}. Мне {age} {get_suff(str(age))}.'
print(message)


first_name = input('Введите фамилию: ')
last_name = input('Введите имя: ')
age = input('Введите возраст: ')
message = f'Привет! Меня зовут {first_name} {last_name}. Мне {int(age)} {get_suff(age)}.'
print(message)
