"""
Задание 1.

Приведен код, который позволяет сохранить в
массиве индексы четных элементов другого массива

Сделайте замеры времени выполнения кода с помощью модуля timeit

Попробуйте оптимизировать код, чтобы снизить время выполнения
Проведите повторные замеры

Добавьте аналитику: что вы сделали и почему
"""


from timeit import Timer

def func_1(nums):
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr

def func_2(nums):
    new_arr= [x for x in nums if x % 2 == 0] #Используем генератор списка
    return new_arr


mass = []
for i in range(10000):
    mass.append(i)
print(func_1(mass))

t1 = Timer("func_1(mass)", "from __main__ import func_1, mass")
t2 = Timer("func_2(mass)","from __main__ import func_2, mass")

print('Time run: ', t1.timeit(number=1000), 'millisecond')
print(func_2(mass))
print('Time run: ', t2.timeit(number=1000), 'millisecond')