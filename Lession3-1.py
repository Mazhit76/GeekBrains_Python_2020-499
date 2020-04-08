"""
1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.
"""
#Функция получает на вхде значеие и производит деление, с проверкоой деления на ноль
def del_us(x,y,err=False):
    err = False
    try:
        z = x / y
        return z
    except ZeroDivisionError:
        err = True
        print ('На ноль делить нельзя!!!!')
        return

#Функция получает на входе значение и проверяет на предмет int или float
def int_in(x, label_float=False, err=False):
    label_float = False
    err = False
    try:
        out=float(x)
    except ValueError:
        err = True
        print('Ща по башке дам...')
        return 0,False,err
    label_float=True
    try:
        out=int(x)
    except ValueError:
        if label_float:
            return out,label_float,err
        err = True
        print('Ща по башке дам...')
        return out, label_float, err
    return out, label_float, err

#Функция запрашивает в циклах ввод первого и второго чисел, проверка int_in
def user_in(err1=False):

    label=True
    try:
        while label:
            user = input('Введите первое число: ')
            user, us_float,err1 = int_in(user, False, err1)
            if err1:
                continue
            else:
                x=user
                break
        while label:
            user = input('Введите второе число: ')
            user, us_float,err1 = int_in(user, False, err1)
            if err1:
                continue
            else:
                y=user
                break
    except:
        print('Введено не число!!!')
    return x, y, err1

err1=False
x,y,err1=user_in()
z=del_us(x,y,err1)
print(z)


