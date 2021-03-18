"""1. Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
Об окончании ввода данных свидетельствует пустая строка.
"""


f_obj = open('task1_file.txt', 'w', encoding='utf-8')
text = []

while '' not in text:
    text.extend([input('Введите текст: '), '\n'])

f_obj.writelines(text)
f_obj.close()
