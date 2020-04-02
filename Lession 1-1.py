one = 'Привет'
two = 23, 55
three = 35
four = True
five = [1, 2, 5, 'Список']
six = (22, 2, 54, 'Кортеж')
seven = {'Name': 'Wasja', 'first_name': 'Pupkin', 'age': 15}

print(type(one))
print(type(two))
print(type(three))
print(type(four))
print(type(five))
print(type(six))
print(type(seven))

name = input('Введите Ваше имя: ')
first_name = input('Введите вашу фамилию: ')
year_byrtday = int(input('Введите год рождения: '))
age = 2020 - year_byrtday
print(f"Здраствуйте {name},{first_name}. Ваш возраст, примерно: {age}")
