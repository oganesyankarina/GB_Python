"""4. Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
При этом английские числительные должны заменяться на русские.
Новый блок строк должен записываться в новый текстовый файл.
"""


words_dict = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}

f_obj = open('task4_file.txt', encoding='utf-8')
text = [line for line in f_obj]
f_obj.close()
print(text)

for item in words_dict.keys():
    text = [line.replace(item, words_dict[item]) for line in text]
print(text)

f_obj = open('task4_file_translate.txt', 'w', encoding='utf-8')
f_obj.writelines(text)
f_obj.close()
