"""
Реализуйте базовый класс Car.
У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда).
Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
Для классов TownCar и WorkCar переопределите метод show_speed.
При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов.
Выполните доступ к атрибутам, выведите результат. Выполните вызов методов и также покажите результат.
"""


class Car:

    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print('go')
        return self

    def stop(self):
        print('stop')
        return self

    def turn(self, direction):
        print(f'turn {direction}')
        return self

    def show_speed(self, print_and_return_self=None):
        if print_and_return_self is None:
            return self.speed
        elif print_and_return_self:
            print(f'{self.speed} km/h')
            return self
        else:
            print(f'ERROR! Unknown argument={print_and_return_self}')

    def __str__(self):
        return f'{self.color} {self.name} {"(Police)" if self.is_police else ""}'


class TownCar(Car):
    def show_speed(self, print_and_return_self=None):
        if print_and_return_self is None:
            return 'Over speed' if self.speed > 60 else str(self.speed)
        else:
            return super().show_speed(print_and_return_self)


class WorkCar(Car):
    def show_speed(self, print_and_return_self=None):
        if print_and_return_self is None:
            return 'Over speed' if self.speed > 40 else str(self.speed)
        else:
            return super().show_speed(print_and_return_self)


class SportCar(Car):
    pass


class PoliceCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, True)


cars = [
    TownCar(50, 'red', 'VW', False),
    WorkCar(50, 'green', 'Peugeot', False),
    SportCar(150, 'red', 'Porsche', False),
    PoliceCar(50, 'white', 'Ford')
]


def test(cars_list):
    for c in cars_list:
        print(f'{c.__str__()} -> {str(c.show_speed())}')


test(cars)

print('*' * 40)

cars[0]\
    .go()\
    .show_speed(True)\
    .turn('left')\
    .turn('right')\
    .stop()
