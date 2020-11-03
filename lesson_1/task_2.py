"""
Пользователь вводит время в секундах.
Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс.
Используйте форматирование строк.
"""

seconds_in_hour = 60 * 60

seconds = int(input('Введите время в секундах: '))

all_seconds = seconds

# полных часов
hours = seconds // seconds_in_hour

# остаток секунд за вычетом полных часов
seconds = seconds - hours * seconds_in_hour

# полных минут
minutes = seconds // 60

# конечный остаток секунд
seconds = seconds - minutes * 60

print(f'{all_seconds} == {hours}:{minutes}:{seconds}')

print(f'Проверка:\n{hours*seconds_in_hour + minutes * 60 + seconds}')
