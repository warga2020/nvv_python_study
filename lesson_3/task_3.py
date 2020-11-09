"""
Реализовать функцию my_func(), которая принимает три позиционных аргумента,
и возвращает сумму наибольших двух аргументов.
"""


def sum_max_pair(a, b, c):
    in_args = [a, b, c]
    in_args.sort(reverse=True)
    return sum(in_args[:2])


print(sum_max_pair(100, 2, 13))
