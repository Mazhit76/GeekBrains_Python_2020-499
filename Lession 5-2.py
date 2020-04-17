"""
2)	Создать текстовый файл (не программно), сохранить в нем несколько строк,
выполнить подсчет количества строк, количества слов в каждой строке.
"""
# Функция получает на входе имя файла в текущей директории и выводит
# списком сумму строк с количтсество слов в каждй строке. Проверка проходит только в типах строковых.
def count_string_in_file(file_us='text.txt'):
    with open(file_us) as file_user:
        list_user=file_user.readlines()
        for i,el in enumerate(list_user):
            count_word=el.count(' ')+1
            print(f'Строка {i+1} слов {count_word} Само слово: {el}')


count_string_in_file()