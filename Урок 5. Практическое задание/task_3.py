"""
Задача 3.
В соответствии с документацией Python,
deque – это обобщение стеков и очередей.
Вот основное правило: если вам нужно что-то быстро дописать или вытащить, используйте deque.
Если вам нужен быстрый случайный доступ, используйте list.

Задача: создайте простой список (list) и очередь (deque).
Выполните различные операции с каждым из объектов.
Сделайте замеры и оцените, насколько информация в документации
соответствует дейстивтельности.
"""
from timeit import timeit
import cProfile
from collections import deque

list_with_range=[i for i in range(1000)]
deq_rang=deque()
deq_rang.extend(list_with_range)

def list_append(num):
    my_list=[]
    for i in range(num):
        my_list.append(i)

def deq_append(num):
    my_list=deque()
    for i in range(num):
        my_list.append(i)

def list_append_left(num):# Самая долгая и тяжелая операция
    my_list=[]
    for i in range(num):
        my_list.insert(0,i)

def deq_append_left(num):# Так себе по скорости
    my_list=deque()
    for i in range(num):
        my_list.appendleft(i)

def list_extend(lst):# Все остальное быстрее
    my_list=[]
    my_list.extend(lst)

def deq_extend(lst):
    my_list=deque()
    my_list.extend(lst)


def list_extend_left(lst):
    my_list=[]
    for i in range(len(lst)):
        my_list.insert(0,i)


def deq_extend_left(lst):
    my_list = deque()
    my_list.extendleft(lst)


def list_pop(lst):
     for i in range(len(lst)):
        a=lst.pop()

def deq_pop(lst):
     for i in range(len(lst)):
        a=lst.pop()


def list_pop_left(lst):
    for i in range(len(lst)):
        a = lst.popleft(0)


def deq_pop_left(lst):
    for i in range(len(lst)):
        a = lst.popleft()

def list_revers(lst):
    a=lst.reverse()

def deq_revers(lst):
    a = lst.reverse()

a=1000
print('list_append--', timeit("list_append(a)", setup="from __main__ import list_append, a", number=1000))
print('deq_append--', timeit("deq_append(a)", setup="from __main__ import deq_append, a", number=1000))
print('deq_append_left--', timeit("deq_append_left(a)", setup="from __main__ import deq_append_left, a", number=1000))
print('list_append_left--', timeit("list_append_left(a)", setup="from __main__ import list_append_left, a", number=1000))
print('list_extend--', timeit("list_extend(list_with_range)", setup="from __main__ import list_extend, list_with_range", number=1000))
print('deq_extend--', timeit("deq_extend(list_with_range)", setup="from __main__ import deq_extend, list_with_range", number=1000))
print('list_pop--', timeit("list_pop(list_with_range)", setup="from __main__ import list_pop, list_with_range", number=1000))
print('deq_pop--', timeit("deq_pop(list_with_range)", setup="from __main__ import deq_pop, list_with_range", number=1000))
print('deq_pop_left--', timeit("deq_pop_left(list_with_range)", setup="from __main__ import deq_pop_left, list_with_range", number=1000))
print('list_pop_left--', timeit("list_pop_left(list_with_range)", setup="from __main__ import list_pop_left, list_with_range", number=1000))
print('list_revers--', timeit("list_revers(list_with_range)", setup="from __main__ import list_revers, list_with_range", number=1000))
print('deq_revers--', timeit("deq_revers(list_with_range)", setup="from __main__ import deq_revers, list_with_range", number=1000))

"""
list_append-- 0.09217911699999999
deq_append-- 0.089853783
deq_append_left-- 0.08699795200000002
list_append_left-- 0.321840304
list_extend-- 0.002152778000000022
deq_extend-- 0.00639001699999997
list_pop-- 0.000510931999999964
deq_pop-- 0.00038327900000001414
deq_pop_left-- 0.0004301070000000129
list_pop_left-- 0.0004086179999999162
list_revers-- 0.00017640399999996337
deq_revers-- 0.00014882100000002119"""