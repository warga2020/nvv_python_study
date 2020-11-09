"""
Программа запрашивает у пользователя строку чисел, разделенных пробелом.
При нажатии Enter должна выводиться сумма чисел.
Пользователь может продолжить ввод чисел, разделенных пробелом и снова нажать Enter.
Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме.
Но если вместо числа вводится специальный символ, выполнение программы завершается.
Если специальный символ введен после нескольких чисел, то вначале нужно добавить сумму этих чисел к полученной ранее сумме
и после этого завершить программу.
"""

global_sum = 0


def calc_str(in_str: str):
    result = 0
    arr = in_str.upper().split('Q')
    tmp_str = arr[0];
    for s in tmp_str.split():
        result += int(s)
    return result, len(arr) > 1


while True:
    s = input('Enter the string of numbers. [Q|q] for exit: ')
    it_sum, isQ = calc_str(s)
    global_sum += it_sum
    print(global_sum)
    if isQ:
        break

print('\nEND')
