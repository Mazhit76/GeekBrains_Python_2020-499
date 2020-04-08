"""
2)	Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя: имя, фамилия, год рождения,
 город проживания, email, телефон. Функция должна принимать параметры как именованные аргументы.
  Реализовать вывод данных о пользователе одной строкой.
"""
#Функция получает на входе данные и возвращает их в виде строки
def str_out(name,second_name,birthday,city,email,tel):
    str_user=(f'Вы ввели: {name} {second_name},{birthday}, {city}, {email},{tel}')
    return str_user
#Функция на входе ничего не получает, на выходе дает данные о пользовате в типе str
def in_user():
    name = input('Введите имя: ')
    second_name=input('Введите фамилию: ')
    birthday=input('Введите дату рождения: ')
    city=input('Введите город проживания: ')
    email=input('Введите е-майл: ')
    tel=input('Введите телефон: ')
    return name,second_name,birthday,city,email,tel


name_us, second_name_us, birthday_us, city_us, email_us, tel_us = in_user()
print(str_out(city=city_us, email=email_us, tel=tel_us, name=name_us, second_name=second_name_us, birthday=birthday_us))
