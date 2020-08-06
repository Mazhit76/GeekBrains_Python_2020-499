"""
7.	Напишите программу, доказывающую или проверяющую, что для множества
натуральных чисел выполняется равенство: 1+2+...+n = n(n+1)/2,
 где n - любое натуральное число.

 Решите через рекурсию. Решение через цикл не принимается.
Для оценки Отлично в этом блоке необходимо выполнить 5 заданий из 7
"""


def recur_method(numb, s=0, m=1):
    if s == m:
        print(f'Равенство: {s==m}')
    elif s < m:
        return recur_method(numb, s + 1, numb * (numb + 1) // 2)


try:
    NUMB = int(input("Введите число: "))
    recur_method(NUMB)
except ValueError:
    print('Вы веди строку, вместо числа! Исправьте.')
