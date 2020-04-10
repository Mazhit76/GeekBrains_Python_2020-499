"""
6)	Реализовать функцию int_func(), принимающую слово из маленьких латинских букв и возвращающую его же,
но с прописной первой буквой. Например, print(int_func(‘text’)) -> Text.
Продолжить работу над заданием. В программу должна попадать строка из слов, разделенных пробелом.
Каждое слово состоит из латинских букв в нижнем регистре. Сделать
вывод исходной строки, но каждое слово должно начинаться с заглавной буквы.
 Необходимо использовать написанную ранее функцию int_func().

"""
#Принимает слово из маленьких латинских букв и возвращающую его же, но с прописной первой буквой
def int_func(str_user):
    return str_user.title()

def in_user(str_user, out_pr=False):
    in_str=input(' ')
    if str_user !='':
        stroke2=str_user+' '+in_str
    else:
        stroke2=in_str
    str_split=stroke2.split(' ')
    for i,n in enumerate(str_split):
        z,err,out_pr=int_in(n)#x, err=False, out_program=False(Это проверка на выход из прогр)
        if ((out_pr == False) and (err == False)):
            str_split[i] = int_func(z)
        else:
            break
    if out_pr:    #Если нажата "N"
        print('Вы нажали "N", значит на выход!!!')
    str_out=' '.join(str_split)
    return str_out, err, out_pr

#Функция получает на входе значение и проверяет на предмет str, если введеное слово ="N",
#  то выход  и  out_program=True
def int_in(x, err=False, out_program=False):
    out_program=False
    err = False
    if ((x == 'n') or (x == 'N')):
        out_program = True
        return 'N', err, out_program  # Если нажали N
    try:
        out=str(x)
    except ValueError:
         if ((x=='n') or (x=='N')):
            out_program=True
            return 'N', err, out_program# Если нажали N
         elif x=='':
             return '', False, False# Если пусто
         else:
            print('Вы ввели не строку...')
            return '',True, False# Если нажали другой формат данных
    return out, False, False

#Функция в цикле опрашивает пользователя пока он не нажмет "N"-выход или Enter-ввод вызов функции in_user,
# проверяет на правильность ввода строки
def input_user(in_str=''):
    result=''
    out_pr=False
    print('Введите строку чисел, разделенных пробелом: ')
    while out_pr==False:
        result,err,out_pr=in_user(str_user=result)
        if err:
            continue
        else:
            print(result,end='')
input_user()