"""
Реализовать проект расчета суммарного расхода ткани на производство одежды.
Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название.
К типам одежды в этом проекте относятся пальто и костюм. У этих типов одежды существуют параметры:
    размер (для пальто) и рост (для костюма). Это могут быть обычные числа: V и H, соответственно.
Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5),
для костюма (2 * H + 0.3). Проверить работу этих методов на реальных данных.
Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания:
    реализовать абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property.
"""

from abc import ABC, abstractmethod


class Clothes(ABC):
    def __init__(self, name, size):
        self.__name = name
        self._size = size

    @abstractmethod
    def _calc_formula(self):
        pass

    @property
    def __material_amount(self):
        return float(f'{self._calc_formula():.2f}')

    def __str__(self):
        return f'Material consumption for "{self.__name}" = {self.__material_amount}'


class Coat(Clothes):
    def _calc_formula(self):
        return self._size/6.5 + 0.5


class Suit(Clothes):
    def _calc_formula(self):
        return 2 * self._size + 0.3


print(Coat('coat_model_1', 33))
print(Suit('suit_model_1', 11))
