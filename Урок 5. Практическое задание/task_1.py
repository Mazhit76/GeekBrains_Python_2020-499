"""
7)	Создать вручную и заполнить несколькими строками текстовый файл, в котором каждая строка должна содержать данные о
 фирме: название, форма собственности, выручка, издержки.
Пример строки файла: firm_1   ООО   10000   5000.
Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
Если фирма получила убытки, в расчет средней прибыли ее не включать
"""
# Функция получает на входе строку содеражащее число  с пробелами с скрытыи знаками на выходе выдает число тип число,
# если пустая, то выдаст 0
"""

def str_count_clear(str_us=''):
    str_out = ''
    for el in str_us:
        if el.isdigit():
            str_out = str_out + el  # Да...забывака...
    return str_out


with open('text_7.txt', encoding='UTF-8') as file_user:
    import json
    try:
        data = file_user.readlines()
        average_profit = 0
        count_profit = 1
        data_out = {}
        for el in data:
            el = el.split('\n')
        summa = 0
        for el in data:
            el = el.split(' ')
            summa_dohoda = int(str_count_clear(el[2]))
            summa_rashoda = int(str_count_clear(el[3]))
            pribil = summa_dohoda - summa_rashoda
            if pribil >= 0:
                average_profit = round(
                    (average_profit + pribil / 12) / count_profit,
                    1)  # Подсчитали среднюю величину дохода на организации
                count_profit = +1
            print(f' {el[0]}    {el[1]}   {summa_dohoda}    {summa_rashoda}  {average_profit}')
            data_out[el[0]] = pribil
        str_out = [data_out] + [{'average_profit': average_profit}]
    except IOError:
        print('Ошибка ввода-вывода')


with open('text_7.json', 'w', encoding='UTF-8') as file_out:
    try:
        # В группе ребята подсказали Moshe Gelberg, так бы долго копался
        json.dump(str_out, file_out, ensure_ascii=False, indent=4)

    except IOError:
        print('Ошибка ввода-вывода')



1.	Пользователь вводит данные о количестве предприятий, их наименования и прибыль
за 4 квартала (т.е. 4 отдельных числа) для каждого предприятия.
Программа должна определить среднюю прибыль (за год для всех предприятий)
и вывести наименования предприятий, чья прибыль выше среднего и отдельно
вывести наименования предприятий, чья прибыль ниже среднего.

Подсказка:
Для решения задачи обязательно примените какую-нибудь коллекцию из модуля collections
Для лучшее освоения материала можете даже сделать несколько решений этого задания,
применив несколько коллекций из модуля collections

Пример:
Введите количество предприятий для расчета прибыли: 2
Введите название предприятия: Рога
через пробел введите прибыль данного предприятия
за каждый квартал(Всего 4 квартала): 235 345634 55 235

Введите название предприятия: Копыта
через пробел введите прибыль данного предприятия
за каждый квартал(Всего 4 квартала): 345 34 543 34

Средняя годовая прибыль всех предприятий: 173557.5
Предприятия, с прибылью выше среднего значения: Рога

Предприятия, с прибылью ниже среднего значения: Копыта
"""
from collections import namedtuple


def input_data():
    profit_aver={}
    count_company=int(input('Ввведите количество предприятий для расчета прибыли:'))
    Companies = namedtuple('Companies', ['name','quart1', 'quart2','quart3','quart4'])
    for i in range(count_company):
        company=Companies(name=input('Название компании:'),
                          quart1 = int(input('Введите прибыль за 1 квартал: ')),
                          quart2 = int(input('Введите прибыль за 2 квартал: ')),
                          quart3 = int(input('Введите прибыль за 3 квартал: ')),
                          quart4 = int(input('Введите прибыль за 4 квартал: ')))
        print(company)
        profit_aver[company.name]=company.quart1+company.quart2+company.quart3+company.quart4
        print(profit_aver)
    total_count = 0
    for value in profit_aver.values():
        total_count=+value
    total_aver=total_count/count_company

    for key,value in profit_aver.items():
        if value>total_aver:
            print(f" {key}-прибыль выше среднего")
        elif value>total_aver:
            print(f" {key}-прибыль ниже среднего")
        else:
            print(f" {key}-прибыль средняя")
input_data()





