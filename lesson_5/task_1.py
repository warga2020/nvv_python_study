"""
Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
Об окончании ввода данных свидетельствует пустая строка.
"""

import os

f_name = os.path.basename(__file__) + '__.txt'

print('Press ENTER to insert text line in file. \nEnter an empty string to complete.')
with open(f_name, 'w') as f:
    while True:
        s = input('> ')
        if len(s) == 0:
            break
        f.write(s + os.linesep)


