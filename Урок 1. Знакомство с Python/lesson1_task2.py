# 2. Пользователь вводит время в секундах.
# Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс.
# Используйте форматирование строк.


sec = int(input('Введите время в секундах: '))
HH = sec//3600
MM = (sec % 3600)//60
SS = (sec % 3600) % 60
print(f'{HH:02}:{MM:02}:{SS:02}')
