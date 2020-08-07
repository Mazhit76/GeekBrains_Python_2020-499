"""
Задание 2.
Ваша программа должна запрашивать пароль
Для этого пароля вам нужно получить хеш, используя функцию sha256
Для генерации хеша обязательно нужно использовать криптографическую соль
Обязательно выведите созданный хеш

Далее программа должна запросить пароль повторно
Вам нужно проверить, совпадает ли пароль с исходным
Для проверки необходимо сравнить хеши паролей

ПРИМЕР:
Введите пароль: 123
В базе данных хранится строка: 555a3581d37993843efd4eba1921f1dcaeeafeb855965535d77c55782349444b
Введите пароль еще раз для проверки: 123
Вы ввели правильный пароль
"""

import uuid, hashlib

salt =uuid.uuid4().hex #Получаем случайного числа перевод в 16 -ти ричную строку


def get_hash(passwd_obj):
    return hashlib.sha256(salt.encode() + passwd_obj.encode()).hexdigest()


def hash_check(hashed_password, user_password):
    return hashed_password == hashlib.sha256(
        salt.encode() + user_password.encode()).hexdigest()


new_passwd = input('Введите пароль: ')
hash_obj = get_hash(new_passwd)
print(f'В базе данных хранится строка: {hash_obj}')

old_pass = input('Введите пароль еще раз, для проверки: ')

if hash_check(hash_obj, old_pass):
    print("Вы ввели правильный пароль!")
else:
    print("Пароль неверный!")
