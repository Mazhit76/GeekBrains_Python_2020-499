"""
Задание 4.
Реализуйте скрипт "Кэширование веб-страниц"

Функция должна принимать url-адрес и проверять
есть ли в кэше соответствующая страница, если нет, то вносит ее в кэш

Подсказка: задачу решите обязательно с применением 'соленого' хеширования
Можете условжнить задачу, реализовав ее через ООП
"""

import uuid
import hashlib

salt = uuid.uuid4().hex  # Получаем случайного числа перевод в 16 -ти ричную строку
cashe_obj = {}


def get_page(url):
    if cashe_obj.get(url):
        print(f'Данный адрес: {url} приисутствует в кэше!')
    else:
        res = hashlib.sha256(salt.encode() + url.encode()).hexdigest()
        cashe_obj[url] = res
        print(cashe_obj)


get_page('https://geekbrains.ru/')
get_page('https://geekbrains.ru/')
get_page('https://geekbrains.ru/')
