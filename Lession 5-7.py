
"""
7)	Создать вручную и заполнить несколькими строками текстовый файл, в котором каждая строка должна содержать данные о фирме: название, форма собственности, выручка, издержки.
Пример строки файла: firm_1   ООО   10000   5000.
Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль. Если фирма получила убытки, в расчет средней прибыли ее не включать

"""
#Функция получает на входе строку содеражащее число  с пробелами с скрытыи знаками на выходе выдает число тип число,
# если пустая, то выдаст 0
def str_count_clear(str_us=''):
    mass=['0','1','2','4','5','6','7','8','9','0','.']

    if not str_us.isdigit():
        str_us=[str_us]
        for i,el in enumerate(str_us):
            if not el in mass:
                str_us[i]=''
    return str_us








with open('text_7.txt', encoding='UTF-8') as file_user:
    import json
    try:
        data=file_user.readlines()
        average_profit=0
        count_profit=1
        for el in data:
            el=el.split('\n')
        summa=0
        for el in data:
            el=el.split(' ')
            summa_dohoda=int(str_count_clear(el[2]))
            summa_rashoda=int(str_count_clear(el[3]))
            print(el[3])
            """
            pribil=summa_dohoda-summa_rashoda
            if pribil>=0:
                average_profit=(average_profit+pribil/12)/count_profit#Подсчитали среднюю величину дохода на организации
                count_profit=+1
            print(f' {el[0]}    {el[1]}   {summa_dohoda}    {summa_rashoda}  {average_profit}')
"""






    except IOError:
        print('Ошибка ввода-вывода')

