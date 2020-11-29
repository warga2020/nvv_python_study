"""
Реализовать класс Stationery (канцелярская принадлежность).
Определить в нем атрибут title (название) и метод draw (отрисовка).
Метод выводит сообщение “Запуск отрисовки.”
Создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер).
В каждом из классов реализовать переопределение метода draw.
Для каждого из классов методы должен выводить уникальное сообщение.
Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.
"""


class Stationery:
    def __init__(self):
        self.title = None

    def draw(self):
        print('Start drawing')


class Pen(Stationery):
    def draw(self):
        print('Draw with pen')


class Pencil(Stationery):
    def draw(self):
        print('Draw with Pencil')


class Handle(Stationery):
    def draw(self):
        print('Draw with Handle')


Pen().draw()
Pencil().draw()
Handle().draw()
