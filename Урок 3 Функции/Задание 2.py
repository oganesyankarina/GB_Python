# 2. Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
# имя, фамилия, год рождения, город проживания, email, телефон.
# Функция должна принимать параметры как именованные аргументы. Реализовать вывод данных о пользователе одной строкой.

name = input('Введите имя: ')
surname = input('Введите фамилию: ')
birth_year = input('Введите год рождения: ')
city = input('Введите город проживания: ')
email = input('Введите email: ')
tel = input('Введите телефон: ')


def get_user_info(**kwargs):
    return kwargs


print(get_user_info(name=name, surname=surname, birth_year=birth_year, city=city, email=email, tel=tel))
