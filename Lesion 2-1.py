def in_mass(mass):
    print ( "Окончание заполнений массива 'None'" )
    user_input = ''
    while user_input != 'None':
        print('1-Ввод целочисленых чисел,2-Ввод чисел с запятой, 3-Ввод строки, 4-Ввод последовательности, 5-Ввод кортеж,','6-Булево значение')
        label=input('Введите вид данных: ')
        user_input = input ( 'Введите значение элемента массива:' )
        label=''
        if user_input == '':
            continue
        elif label == '1':
            mass.append ( int ( user_input ) )
        elif label == '2':
            mass.append ( float ( user_input ) )
        elif label == '3':
            mass.append  ( user_input )
        elif label == '4':
            mass.extend ( list ( user_input ) )
        elif label == '5':
            mass.append ( tuple ( user_input ) )
        elif (label == '6') and ((user_input=='True') or(user_input=='False')):
            mass.append(True if user_input=='True' else False)
    return mass
mass = [57676, 8.46, 'Привет Мажит', 'л',[74674], 'о', 'п', 'л',False, 'к', '3', {'rfg':'75','7557':'ryr'},'4', '3', ('Б', 'Ь', 'В', 'А', 'О', 'К', '7', '4'), 'True', False]
def check_mass_type(mass):
    for i in mass:
      print (f'{type(i)}-----{i}')










in_mass ( mass )
check_mass_type(mass)
print(type(mass))
