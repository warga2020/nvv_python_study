"""
Создать текстовый файл (не программно), сохранить в нем несколько строк,
выполнить подсчет количества строк, количества слов в каждой строке.
"""

fname = 'task_2__.txt'

with open(fname) as f:
    lines = f.readlines()
    print(f'File "{fname}"\nlines count: {len(lines)}')
    for i, ln in enumerate(lines, 1):
        print(f'line #{i} -> {len(ln.split())} words.')





