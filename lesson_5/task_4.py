"""
Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
При этом английские числительные должны заменяться на русские.
Новый блок строк должен записываться в новый текстовый файл.
"""
import os

rus_num = ('', 'один', 'два', 'три', 'четыре')

f_src = open('task_4__.src')
f_dst = open('task_4__.dst', 'w')
try:
    for line in f_src:
        a, x, b = line.strip().split(' ')
        ru_text = [rus_num[int(b)], x, b, os.linesep]
        f_dst.write(' '.join(ru_text))
finally:
    f_src.close()
    f_dst.close()
