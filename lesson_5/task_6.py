"""
Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет и наличие лекционных,
практических и лабораторных занятий по этому предмету и их количество.
Важно, чтобы для каждого предмета не обязательно были все типы занятий.
Сформировать словарь, содержащий название предмета и общее количество занятий по нему.
Вывести словарь на экран.

Примеры строк файла:
Информатика: 100(л) 50(пр) 20(лаб).
Физика: 30(л) — 10(лаб)
Физкультура: — 30(пр) —

Пример словаря:
{“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}
"""
import os
import json

f_name_base = os.path.basename(__file__).split('.')[0] + '.base'
f_name_json = os.path.basename(__file__).split('.')[0] + '__.json'

with open(f_name_base) as f:
    subjects = {}
    for line in f:
        subj, data = line.split(':')
        hours = [x.split('(')[0] for x in data.split()]
        hours = [int(x) for x in hours if x.isdigit()]
        subjects[subj] = sum(hours)

    with open(f_name_json, 'w') as f_json:
        json.dump(subjects, f_json, ensure_ascii=False)

with open(f_name_json) as f:
    s = json.load(f)
    print(f'\n{f_name_json} >>  {s}')


