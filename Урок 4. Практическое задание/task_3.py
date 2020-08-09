"""
Задание 3.

Приведен код, формирующий из введенного числа
обратное по порядку входящих в него
цифр и вывести на экран.

Сделайте профилировку каждого алгоритма через cProfile и через timeit

Сделайте вывод, какая из трех реализаций эффективнее и почему
"""
from timeit import timeit
import cProfile


def revers(enter_num, revers_num=0):
    if enter_num == 0:
        return enter_num,revers_num
    else:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
        revers(enter_num, revers_num) # O(2^n)+сильно ограничение по стеку


def revers_2(enter_num, revers_num=0):
    while enter_num != 0:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
    return revers_num               # O(2^n)+сильно ограничение по стеку


def revers_3(enter_num):# Самая эффективная функция исходя из расчета времени
    enter_num = str(enter_num)
    revers_num = enter_num[::-1]
    return revers_num               #Срез, списка O(n)

def my_f(a):
    print(revers(a))
    print(revers_2(a))
    print(revers_3(a))




a=int(input("Input count:"))
c=list(range(a))
a=int(''.join(map(str, c)))
print(a)

print(timeit("revers(a)", setup="from __main__ import revers, a", number=1000))
print(timeit("revers_2(a)", setup="from __main__ import revers_2, a", number=1000))
print(timeit("revers_3(a)", setup="from __main__ import revers_3, a", number=1000))


cProfile.run('my_f(a),a')