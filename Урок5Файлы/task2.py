"""2. Создать текстовый файл (не программно), сохранить в нем несколько строк,
выполнить подсчет количества строк, количества слов в каждой строке.
"""


f_obj = open('task2_file.txt', encoding='utf-8')
text = [line.strip() for line in f_obj]
f_obj.close()

print(f'Количество строк в файле: {len(text)}')
for line in text:
    print(f'Строка: {line}')
    print(f'Количество слов в строке: {len(line.split())}')
