"""
Задача 4.
Поработайте с обычным словарем и OrderedDict.
Выполните различные операции с каждым из объектов и сделайте замеры.
Опишите полученные результаты, сделайте выводы."""

from collections import OrderedDict
from timeit import timeit
from functools import wraps
import time
dict_one = {str(i): i for i in reversed(range(9999))}  # Обычный словарь
dict_two = {str(i): i for i in reversed(range(10,9999))}  # Обычный словарь  для работы на с  словарями
dict_order = OrderedDict(sorted(dict_one.items()))  # Экземпляр OrderedDict

print(dict_one)
#print(dict_two)
print(dict_order)


"""
def time_it(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        func(args[0])
        print(time.time() - start_time)
    return wrapper
"""

# Взято с ичточника https://tirinox.ru/useful-decorators/ там описаны ещй много декораторов,которые могут пригодться в работе

def timeit(method):
    @wraps(method)
    def timed(*args, **kw):
        ts = time.monotonic()
        result = method(*args, **kw)
        te = time.monotonic()
        ms = (te - ts) * 1000
        all_args = ', '.join(tuple(f'{a!r}' for a in args)
                             + tuple(f'{k}={v!r}' for k, v in kw.items()))
        print(f'{method.__name__}({all_args}): {ms:2.2f} ms')
        return result
    return timed
# использование:
"""
@timeit
def slow_func(x, y, sleep):
    time.sleep(sleep)
    return x + y
slow_func(10, 20, sleep=2)
# печатает: slow_func(10, 20, sleep=2): 2004.65 ms


@timeit
def replace_dict_one():
    pass
@timeit
def replace_dict_order():
    pass
"""
@timeit
def update_dict_one(dict_one, dict_two):
    dict_three=dict_one.update(dict_two)
    #print(dict_three)

@timeit
def update_dict_order(dict_order, dict_two):
    dict_four=dict_order.update(OrderedDict(sorted(dict_two.items())))
    #print(dict_four)



@timeit
def get_dict_one(count):
    dict_obj = {str(i): i for i in (range(count))}# Ввиду того, что обе словаря и упорядоченный и не упорядоченный работатют
    #print(dict_obj)                              # с элементами массива как ссылками на объект, то в обеих случаях это просходит быстро

@timeit
def get_dict_order(count):
    dict_order= OrderedDict({str(i): i for i in range(count)})# Но в этом случае это отсортированный по возрастаню значений
    #print(dict_order)                                        #словарь, на сортировку уходит времени, но это компенсируется тем, что с ним очень удобно работать.
                                                              # вывод при больших данных и частых их обменов данных данный способ не подходит


count=1000000

get_dict_one(count)
get_dict_order(count)
update_dict_one(dict_one,dict_two)
update_dict_order(dict_order, dict_two)

"""
@timeit
def pop_dict_one():
    pass
@timeit
def pop_dict_order():
    pass
"""

