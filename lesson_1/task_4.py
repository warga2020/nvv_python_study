"""
Пользователь вводит целое положительное число.
Найдите самую большую цифру в числе.
Для решения используйте цикл while и арифметические операции.
"""

num = int(input('Введите число: '))

max_digit = 0

while True:
    digit = num % 10
    if digit > max_digit:
        max_digit = digit
    if digit == num:
        break
    else:
        num = int(num / 10)

print(f'MAX({num}) --> {max_digit}')