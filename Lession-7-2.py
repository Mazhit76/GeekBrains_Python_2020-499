"""
2)	Реализовать проект расчета суммарного расхода ткани на производство одежды. Основная сущность (класс) этого проекта
 — одежда, которая может иметь определенное название. К типам одежды в этом проекте относятся пальто и костюм.
 У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма).
 Это могут быть обычные числа: V и H, соответственно.
Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5),
для костюма (2*H + 0.3). Проверить работу этих методов на реальных данных.
Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания:
реализовать абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property.

"""
from abc import ABC,abstractmethod

class Clothes(ABC):
    def __init__(self, name=''):
        self.name=name


    @abstractmethod
    def fabric_consuption(self):
        pass

class Coat(Clothes):
    def __init__(self,about=45):
        self.about=about

    count=input("Можете ввести размер пальто, по умолчанию 45 рамер:")
    if count !='':about=int(count)

    @property
    def fabric_consuption(self):
        return round((self.about/6.5+0.5),2)


class Suit(Clothes):
    def __init__(self,hight=45):
        self.hight=hight
    count=input("Можете ввести размер костюма, по умолчанию 45 рамер:")
    if count !='':hight=int(count)
    @property
    def fabric_consuption(self):
        return round((2*self.hight+0.3),2)

palto=Coat(45)
kostum=Suit(45)
print(palto.fabric_consuption)
print(kostum.fabric_consuption)
print('На костюм меньше ткани ушло') if palto.fabric_consuption >= kostum.fabric_consuption else print('На пальто меньше ткани ушло')



