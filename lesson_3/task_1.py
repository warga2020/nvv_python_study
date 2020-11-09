"""
Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.
"""


def my_div(a, b):
    try:
        return a, b, a / b
    except ZeroDivisionError as e:
        return f'ERROR! {e}'


def get_num():
    return int(input(f'Enter the number:'))


a, b, result = my_div(get_num(), get_num())
print(f'Result of {a}/{b} = {result}')
