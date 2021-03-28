"""2. Реализовать проект расчета суммарного расхода ткани на производство одежды.
Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название.
К типам одежды в этом проекте относятся пальто и костюм.
У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма).
Это могут быть обычные числа: V и H, соответственно.
Для определения расхода ткани по каждому типу одежды использовать формулы:
для пальто (V/6.5 + 0.5), для костюма (2 * H + 0.3). Проверить работу этих методов на реальных данных.
Реализовать общий подсчет расхода ткани.
Проверить на практике полученные на этом уроке знания:
реализовать абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property.
"""
from abc import ABC, abstractmethod


class AbstractClothes(ABC):
    @abstractmethod
    def __init__(self):
        pass

    @property
    def tissue_consumption(self):
        pass

    def __add__(self, other):
        return self.tissue_consumption + other.tissue_consumption


class Coat(AbstractClothes):
    def __init__(self, size):
        self.size = size
        self._tissue_consumption = None

    @property
    def tissue_consumption(self):
        self._tissue_consumption = round(self.size/6.5 + 0.5, 2)
        return self._tissue_consumption


class Suit(AbstractClothes):
    def __init__(self, height):
        self.height = height
        self._tissue_consumption = None

    @property
    def tissue_consumption(self):
        self._tissue_consumption = round(2 * self.height + 0.3, 2)
        return self._tissue_consumption


if __name__ == '__main__':
    my_coat = Coat(42)
    my_suit = Suit(1.62)

    print(f'Расход ткани для пальто: {my_coat.tissue_consumption}')
    print(f'Расход ткани для костюма: {my_suit.tissue_consumption}')
    print(f'Общий расход ткани: {my_coat + my_suit}')

    pass
