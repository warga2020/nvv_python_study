"""
Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
"""
import random as rnd

tmp_file = 'task_5__.tmp'

with open(tmp_file, 'w') as f:
    f.write(' '.join([str(rnd.randint(1, 100)) for i in range(10)]))

f = open(tmp_file)
try:
    print(f.read())
    f.seek(0)
    int_list = [int(x) for x in f.read().split()]
    print(f'SUM={sum(int_list)}')
finally:
    f.close()
