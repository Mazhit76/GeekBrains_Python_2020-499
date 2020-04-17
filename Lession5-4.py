"""
4)	Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
При этом английские числительные должны заменяться на русские.
Новый блок строк должен записываться в новый текстовый файл.

"""
#Функция принимает на входе название файла,формат txt, по умолчанию text_4.txt, открывает его,
# построчно берет строки и числительные переводит на
# английский слова перевода берет из функции перевода, далее создает такой же файл
# добавля к имени пути "_lang", формат "txt"


def translation_user(f_translation='text_4.txt'):
    try:
        with open(f_translation)as user_file:
            mass = user_file.readlines()
            for i, el in enumerate(mass):
                el_i = el.replace(' ', '').replace('\n','').split('-')  # Избавились от перевода сроки и разделили по пробелу на части
                el_i[1]=number_translation(el_i[1])#Присваиваем значению цифры перевод из словаря
                mass[i]=el_i
        with open(f_translation.replace('.txt','_lang.txt'), 'w', encoding='UTF-8') as out_file:
            for i in mass:
                str_out=(f'{i[0]}-{i[1]}\n')
                out_file.write(str_out)
    except IOError:
        print("Ошибка ввода-вывода")

#Функция принимает на входе число и выдает его обозначение на русском языке
def number_translation(str_user, lang_str=''):
    languege_book={'1':'один','2':'два','3':'три','4':'четыре'}
    if str_user in languege_book:
        lang_str=languege_book[str_user]
    else:
        lang_str='Элемент не найден'
    return lang_str


translation='text_4.txt'
translation_user(translation)