"""
Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск).
Атрибут реализовать как приватный. В рамках метода реализовать переключение светофора в режимы: красный, желтый, зеленый.
Продолжительность первого состояния (красный) составляет 7 секунд, второго (желтый) — 2 секунды,
третьего (зеленый) — на ваше усмотрение.  Переключение между режимами должно осуществляться только
 в указанном порядке (красный, желтый, зеленый). Проверить работу примера, создав экземпляр и вызвав описанный метод.
Задачу можно усложнить, реализовав проверку порядка режимов, и при его нарушении выводить соответствующее
сообщение и завершать скрипт.

"""
import time
from tkinter import *
class Traficlight:#Create class
    def __init__(self):
        self.__color='Красный' #create atribute of class

    def running(self, color):#create metod of class

        def out_(light,us_timer):
            if light=='Красный': el='\r\033[41m'
            elif light=='Желтый': el='\r\033[43m'
            elif light=='Зеленый': el='\r\033[42m'
            print(f'{el}{self.__color}',end='')
            time.sleep(us_timer)

        color_count=0
        while True:
            self.__color='Красный'
            out_(self.__color,7)
            self.__color='Желтый'
            out_(self.__color,2)
            self.__color='Зеленый'
            out_(self.__color,5)
            self.__color='Желтый'
            out_(self.__color,2)
            color_count=color_count+1
            print("    ",color_count, end='')
            time.sleep(2)


a=Traficlight()#Create objekt class of Traficlight
a.running('Желтый')
