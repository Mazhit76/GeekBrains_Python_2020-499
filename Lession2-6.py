def in_user(user_list=[], mass={}):
    mass={'наименование': 'комьютер', 'цена': '50000', 'Количество': '1', 'ед': 'шт'}
    label=True

    while label:
        if input('Вводим данные: Yes/No: ') =='No':
            break
        mass.update(dict(наименование=input('Введите название товара:')))
        mass.update(dict(цена=input('Введите стоимость: ')))
        mass.update(dict(Количество=input('Введите количество: ')))
        mass.update(dict(ед=input('Единица измерения: ')))
        i = len(user_list) + 1
        user_turpl=i, mass.items()
        user_list.append(user_turpl)
    return user_list

def analitik(user_list):
       for i in user_list:
           print (i[1])

user_list=[]
in_user(user_list)
analitik(user_list)