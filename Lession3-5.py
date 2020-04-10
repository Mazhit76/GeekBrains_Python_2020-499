"""
Программа запрашивает у пользователя строку чисел, разделенных пробелом.
При нажатии Enter должна выводиться сумма чисел.
Пользователь может продолжить ввод чисел, разделенных пробелом и снова нажать Enter.
Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме.
Но если вместо числа вводится специальный символ, выполнение программы завершается.
Если специальный символ введен после нескольких чисел,
то вначале нужно добавить сумму этих чисел к полученной ранее сумме и после этого завершить программу.
"""
# Функция На входе получает строку введеную ранее,  опрашивает пользователя и получает строку в виде чисел
# разделенных пробелами, добавляает ее после ранее введенной
#  и разделяет их по пробелу. Далее в цикле по количесву
# элементов суммирует их в summa возвращает в типе строка
def in_user(str_user, out_pr=False):
    summa=0
    stroka1=str_user
    in_str=input(' ')
    stroke2=stroka1+' '+in_str
    str_split=stroke2.split(' ')
    for i,n in enumerate(str_split):
        i,lb_fl,err,out_pr=int_in(n)#x, label_float=False, err=False, out_program=False(Это проверка на выход из прогр)
        if ((out_pr==False) and (err==False)):
            summa=summa+i
        else:
            break
    if out_pr:    #Если нажата "N"
        print('Вы нажали "N", значит на выход!!!')
    return str(summa),out_pr

#Функция получает на входе значение и проверяет на предмет int или float, если введеное слово ="N",
#  то выход  и  out_program=True
def int_in(x, label_float=False, err=False, out_program=False):
    out_program=False
    label_float = False
    err = False
    try:
        out=float(x)
    except ValueError:
        err = True
        if ((x=='n') or (x=='N')):
            out_program=True
            return 0, label_float, err, out_program# Если нажали N
        elif x=='':
            out_program=False
            out=0
            err=False
            return 0, label_float, err, out_program# Если пусто

        else:
            print('Вы ввели не число...')
            return 0,False,err, out_program# Если нажали друние символы
    label_float=True
    try:
        out=int(x)
    except ValueError:
        if label_float:
            return out,label_float,err, out_program
        err = True
        if ((x=='n') or (x=='N')):
            out_program=True
            return 0, label_float, err, out_program# Если нажали N
        elif x=='':
            out_program=False
            out=0
            err=False
            return 0, label_float, err, out_program# Если пусто
        else:
            print('Вы ввели не число...')
            return 0,False,err, out_program# Если нажали друние символы
    return out, label_float, err, out_program

#Функция в цикле опрашивает пользователя пока он не нажмет "N"-выход или Enter-ввод вызов функции in_user
def input_user(in_str=''):
    result=''
    out_pr=False
    print('Введите строку чисел, разделенных пробелом, N-Out: ')
    while out_pr==False:
        result,out_pr=in_user(str_user=result)
        print(result,end='')

input_user()

