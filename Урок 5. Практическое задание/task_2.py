"""
2.	Написать программу сложения и умножения двух шестнадцатеричных чисел.
При этом каждое число представляется как массив, элементы которого это цифры числа.
Например, пользователь ввёл A2 и C4F. Сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].

Подсказка:
Для решения задачи обязательно примените какую-нибудь коллекцию из модуля collections
Для лучшее освоения материала можете даже сделать несколько решений этого задания,
применив несколько коллекций из модуля collections
Также попробуйте решить задачу вообще без collections и применить только ваши знания по ООП
(в частности по перегрузке методов)

import collections
import functools

def calculate():
    nums=collections.defaultdict(list)
    for m in range(2):
        n= input(f"Введите {m+1}-е шестнадцатиричное число:  ")
        nums[f'{m+1}-{n}']=list(n)
    print(nums)

    summa=sum([int(''.join(i),16) for i in nums.values()])
    print('Сумма: ', list('%X' % summa))

    mult=functools.reduce(lambda a,b,: a*b, [int(''.join(i),16) for i in nums.values()])
    print('', list('%X' % summa))
calculate()
"""

class HexOPeration:
    def __init__(self, num_first, num_second):
        self.num_first= num_first
        self.num_second= num_second
    def __add__(self, other):
        return list(hex(int(''.join(self.num_first),16)+int(''.join(self.num_second),16)))
    def __mul__(self, other):
        return list(hex(int(''.join(self.num_first), 16) * int(''.join(self.num_second), 16)))
num_first = list(input(('Введите первое шестнадцатиречное число: ')))
num_second = list(input(('Введите второе шестнадцатиречное число: ')))

res_sum=HexOPeration(num_first, num_second)+HexOPeration(num_first, num_second)
res_mul=HexOPeration(num_first, num_second)*HexOPeration(num_first, num_second)

print(f'Сумма чисел={res_sum}\n Произведение чисел= {res_mul}')