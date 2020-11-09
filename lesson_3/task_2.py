"""
Реализовать функцию, принимающую несколько параметров,
описывающих данные пользователя: имя, фамилия, год рождения, город проживания, email, телефон.
Функция должна принимать параметры как именованные аргументы.
Реализовать вывод данных о пользователе одной строкой.
"""


def person_info(name, surname, birth_year, city, email, phone):
    print('PERSON: ' + ', '.join(map(lambda x: str(x), locals().values())))


person_info(
    name='Name',
    surname='Surname',
    birth_year=1111,
    city='Minsk',
    email='belarus@gmail.com',
    phone='+375111111111'
)
