"""
6)	Реализовать два небольших скрипта:
а) итератор, генерирующий целые числа, начиная с указанного,
б) итератор, повторяющий элементы некоторого списка, определенного заранее.

Подсказка: использовать функцию count() и cycle() модуля itertools.
 Обратите внимание, что создаваемый цикл не должен быть бесконечным.
 Необходимо предусмотреть условие его завершения.
Например, в первом задании выводим целые числа, начиная с 3, а при достижении числа 10 завершаем цикл.
Во втором также необходимо предусмотреть условие, при котором повторение элементов списка будет прекращено.

"""

from functools import partial,reduce
from itertools import cycle, count


# Фунция возвращает во время исполнения цикла значеие элемента цикла в порядке увеличения от числа полученного на входе  user_count до числа max_count,
# по умолчанию он установлен да 100.
def sequence_up_to_100(user_count, max_count=100):
    for i in count(user_count):
        if i > max_count:
            break
        else:
            yield i
    return


# Фунция возвращает во время исполнения цикла значеие цикла- элемент последовательности полученный на входе,
# количество проходов полученных на входе max_cycle по умолчанию 50 .
def sequence_element(user_list, max_cycle=50):
    count_cycle = 0
    for j in cycle(user_list):
        if count_cycle > max_cycle:
            break
        else:
            count_cycle += 1
            yield j
    return
if __name__=='__main__':
    user_len=98# Переменная от которой будет начинаться последовательность
    user_cycle=25# Переменная длины повторной последовательности
    user_str=list(sequence_up_to_100(user_len))
    print(list(sequence_element(user_str,user_cycle)))
    cycle_user_str=cycle(user_str)
    for i in range(0,len(user_str)):
        print(f'{i+1} элемент, значение {next(cycle_user_str)}')