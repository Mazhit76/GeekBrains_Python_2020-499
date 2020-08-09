"""
Задание 2.

Приведен код, который формирует из введенного числа
обратное по порядку входящих в него цифр.
Задача решена через рекурсию

Сделайте замеры времени выполнения кода с помощью модуля timeit

Попробуйте оптимизировать код, чтобы снизить время выполнения
Проведите повторные замеры

Подсказка: примените мемоизацию

Добавьте аналитику: что вы сделали и почему
"""
import timeit

def memorize(func):# Мемоизация позволяет записывать произведнный вычисления в память и при совпадении входных
    # паратров, просто берет из памяти, я не вычисляет, так O(2 ^n)-->O(2n)
    def g(n, memory={}):
        r = memory.get(n)
        if r is None:
            r = func(n)
            memory[n] = r
        return r
    return g

def recursive_reverse1(number):
    if number == 0:
        return str(number % 10)
    return f'{str(number % 10)}{recursive_reverse(number // 10)}'# O(2 ^n)

@memorize
def recursive_reverse(number):
    if number == 0:
        return str(number % 10)
    return f'{str(number % 10)}{recursive_reverse(number // 10)}' #O (2n)

n=int(input('Введите число: '))
print(recursive_reverse1(n))
print(timeit.timeit("recursive_reverse1(n)", setup="from __main__ import recursive_reverse1, n"))
print(timeit.timeit("recursive_reverse(n)", setup="from __main__ import recursive_reverse, n"))