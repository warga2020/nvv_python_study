"""
Поработайте с переменными, создайте несколько, выведите на экран,
запросите у пользователя несколько чисел и строк и сохраните в переменные, выведите на экран.
"""

var_int = 123
var_str = 'qwerty'
var_float = 3.14
var_bool = True

print('Имя переменной "%s". Тип "%s". Значение "%s"' % ('var_float', type(var_float), str(var_float)))

city = input('\nВведите название города: ')
year = int(input('Введите год: '))

print('\nГород: {}.\nГод: {}'.format(city, year))

print(f'\nДиская смесь --> '
      f'{str(int(var_int * var_float // 2))}-'
      f'{var_str}-'
      f'{var_bool}')



