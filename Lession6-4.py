"""
4)	Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
  А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда).
  Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar. Добавьте в базовый класс метод show_speed,
  который должен показывать текущую скорость автомобиля. Для классов TownCar и WorkCar переопределите метод show_speed.
  При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
Выполните вызов методов и также покажите результат.

"""
class Car:
    def __init__(self, speed=0, color='белая', name='ВАЗ', bool=False):
        self.speed=speed
        self.color=color
        self.name=name
        self.is_police=bool
        polis='Полицеская'if self.is_police else ''
        if self.speed !=0: print(f'Марка машины: {self.name} Цвет: {self.color} Скорость: {self.speed}, {polis}')

    def go(self):
        print("Машина поехала")
    def stop(self):
        print("Машина остановилась")
    def left(self):
        print("Машина повернула влево")
    def right(self):
        print("Машина повернула направо")

    def show_speed(self):
        print(f"Скорость автомобиля составляет {self.speed}")

class TownCar(Car):
    def show_speed(self):
        if self.speed>60:
            count=self.speed-60
            print(f'Скорость {self.speed}, превышение скорости на {count}')
        else:
            print(f"Скорость автомобиля составляет {self.speed}")


class SportCar(Car):
    pass

class WorkCar(Car):
    def show_speed(self):
        if self.speed>40:
            count=self.speed-40
            print(f'Скорость {self.speed}, превышение скорoсти на {count}')
        else:
            print(f"Скорость автомобиля составляет {self.speed}")

class PoliceCar(Car):
    pass
"""    def __init__(self, speed,color,name,bool):


        self.speed=speed
        self.color=color
        self.name=name
        self.is_police=bool
        polis='Полицеская'if self.is_police else ''
        if self.speed !=0: print(f'Марка машины: {self.name} Цвет: {self.color} Скорость: {self.speed}, {polis}')
"""

from random import choice,randint
"""
a_car=Car(100,'Белый','Ferrary',False)
a_car.show_speed()

a_ferrary=SportCar(105,'Красный','Ferrary',True)
a_ferrary.show_speed()

a_town=TownCar(112,'Желтый','КАМАЗ',False)
a_town.show_speed()

a_work=WorkCar(122,'Синий','Беларус',False)
a_work.show_speed()


"""

mass=['go', 'stop','right', 'left']
mass_car=['ferrary','car','polis','town','work']
a=Car()
for i in range(1,10):
    do=choice(mass)#Выбор дейстивя авто
    choice_car=choice(mass_car)#Выбор марка авто
    user_sped=randint(0,150)# Установили скорость

    if choice_car=='car':
        a_car=Car(user_sped,'Белый','ВАЗ',False)
        a_car.show_speed()# В зависимости от того какая машина, выбираем переопределенный метод(не везде он переопрделен)
    elif choice_car=='ferrary':
        a_ferrary=SportCar(user_sped,'Красный','Ferrary',False)
        a_ferrary.show_speed()
    elif choice_car=='town':
        a_town=TownCar(user_sped,'Желтый','КАМАЗ',False)
        a_town.show_speed()
    elif choice_car=='polis':
        a_polis=PoliceCar(user_sped,'Белый','Lada',True)
        a_polis.show_speed()
    else:
        a_work=WorkCar(user_sped,'Синий','Беларус',False)
        a_work.show_speed()
    if do=='go': a.go()         #В зависимости от того какое действие выбираем метод действие: left,right,stop,go
    elif do=='left': a.left()
    elif do=='right': a.right()
    else:a.stop()

    print()# Пустая строка
