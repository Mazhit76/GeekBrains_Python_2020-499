"""
3)	Создать текстовый файл (не программно), построчно записать фамилии сотрудников и
величину их окладов (не менее 10 строк). Определить, кто из сотрудников имеет оклад менее 20 тыс.,
вывести фамилии этих сотрудников. Выполнить подсчет средней величины дохода сотрудников.
Пример файла:
Иванов 23543.12
Петров 13749.32

"""
#Функция получает на входе файл, по умолчани. text_3.txt. Выводит список сотрудников с з/п менее 20 000
def salary_user(file_user='text_3.txt'):
    try:
        with open(file_user, encoding="UTF-8") as us_file:
            mass=us_file.readlines()
            for i,el in enumerate(mass):
                el_i=el.replace('\n','').split(' ')#Избавились от перевода сроки и разделили по пробелу на части
                salary=float(el_i[1])
                if salary<=20000:
                    print(f'Сорудник: {el_i[0]}, зарплата: {el_i[1]} рублей доход в месяц: {round(salary-salary*0.13,2)} рублей')
    except IOError:
        print("Ошибка ввода-вывода")

salary_user()