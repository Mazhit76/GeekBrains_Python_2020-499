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

import timeit
import deque from collections

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

def list_append_left(num):
    my_list=[]
    for i in range(num):
        my_list.insert(0,i)

def deq_append_left(num):
    my_list=deque()
    for i in range(num):
        my_list.appendleft(i)

def list_extend(lst):
    my_list=[]
    my_list.extend(lst)

def deq_extend(lst):
    my_list=deque()
    my_list.extend(lst)


def list_extend_left(lst):
    my_list=[]
    for i in range(lst):
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