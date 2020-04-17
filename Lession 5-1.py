"""
Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
Об окончании ввода данных свидетельствует пустая строка.
"""
#Функция на входе получает список, по умолчанию список пустой, куда вставлять текст в виде списка. На выходе в виде
# сиска с построковыми элемнтами
def in_user(str_out=[]):
    str_out=[]
    while True:
        str_user=input("Введите текст. Окончание пустая строка.")
        if str_user=='':
            break
        else:
            str_out.append(str_user)
    return str_out
#Функция на входе получает список с построковыми элементами и записывет их в файл по строкам с пробелами.
# Назание которого запрашивает у пользователя. Если поьзователь ввел пустую строку, то файл по умолчанию:
#  text.txt, строка пустая="".
def str_in_file( str_out='',file_name='text.txt'):
    try:
        file_user=input('Введите назавание файла куда сохраним текст: ')
        if file_user !='':
            file_name=file_user
        with open(file_name,'x')as file_out:
            file_name.write(str_out)
    except IOError:
        print("Ошибка ввода-вывода")
        with open(file_name,'a') as file_out:
            for el in str_out:
                file_out.write('\n'+el)
            print("Есть такой файл, мы в него дописали")





str_user=in_user()
print(str_user)
str_in_file(str_user)