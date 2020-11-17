"""
Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
Выполнить подсчет средней величины дохода сотрудников.
"""

f = open('task_3__.base')
try:
    f_lines = [line.split() for line in f]
    print(f_lines)
    low_list = [it for it in f_lines if int(it[1]) < 20000]
    print(f'Salary < 20_000: {[it[0] for it in low_list]}')
    slr_list = [int(it[1]) for it in f_lines]
    print(f'Average salary: {sum(slr_list) / len(slr_list)}')
finally:
    f.close()

