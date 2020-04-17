"""
5)	Создать (программно) текстовый файл, записать в него программно набор чисел,
 разделенных пробелами.
Программа должна подсчитывать сумму чисел в файле и выводить ее на экран
"""
from random import random,choice
with open('text_5.txt', 'w',encoding='UTF-8') as out_file:
    for i in range(1,10):
        out_file.write(str(round(random()*1000,2)*choice([-1,1]))+' ')#Сформировали файд text_5.txt и заполнили е сл.числами
with open('text_5.txt', 'r',encoding='UTF-8') as out_file:
    summa=0
    mass=(out_file.readlines())
    for el in mass:
        el_i=el.split(' ')
    for el in el_i:
        if (not(el=='') and not(el.isspace())):#Исключаем все неотображаемые символы и пустышки
            summa=+float(el)
        print(summa)



