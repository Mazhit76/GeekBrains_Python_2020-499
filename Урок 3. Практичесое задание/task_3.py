"""
Задание 3.
Определить количество различных подстрок с использованием хеш-функции.
Дана строка S длиной N, состоящая только из строчных латинских букв.

Подсказка: примените хеши и множества

рара:

рар
ра
ар
ара
р
а
"""

import hashlib
from collections import Counter

stroka = input('Введите строку из маленьких букв: ')

unic_stroka = set()
N = len(stroka)
for i in range(N):
    if i == 0:
        N = len(stroka) - 1
    else:
        N = len(stroka)
    for j in range(N, i, -1):
        print(stroka[i:j])
        unic_stroka.add(hashlib.sha1(stroka[i:j].encode('utf-8')).hexdigest())
print(unic_stroka)

print(
    "Количество различных подстрок в в строку '%s' равно %d" %
     (stroka, len(unic_stroka)))
