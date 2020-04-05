def in_mass(mass_user=[57676, 8.46, 'Привет Мажит', 'л',[74674], 'о', 'п', 'л',False, 'к', '3', {'rfg':'75','7557':'ryr'},'4', '3', ('Б', 'Ь', 'В', 'А', 'О', 'К', '7', '4'), 'True', False]):
    print ( "Окончание заполнений массива 'None'" )
    user_input = ''
    while user_input != 'None':
        print (
            '1-Ввод целочисленых чисел,2-Ввод чисел с запятой, 3-Ввод строки, 4-Ввод последовательности, 5-Ввод кортеж,',
            '6-Булево значение' )
        label = ''
        label = input ( 'Введите вид данных: ' )
        user_input = input ( 'Введите значение элемента массива:' )
        if user_input == '':
            continue
        elif label == '1':
            mass_user.append ( int ( user_input ) )
        elif label == '2':
            mass_user.append ( float ( user_input ) )
        elif label == '3':
            mass_user.append ( user_input )
        elif label == '4':
            mass_user.extend ( list ( user_input ) )
        elif label == '5':
            mass_user.append ( tuple ( user_input ) )
        elif (label == '6') and ((user_input == 'True') or (user_input == 'False')):
            mass_user.append ( True if user_input == 'True' else False )
    return mass_user


def rev_el(mass_user, mass_o):
    mass_o = []
    mass_user = mass
    max_len=len(mass_user)
    for ind, el in enumerate ( mass_user ):
        if (ind % 2 == 0):
            if ((ind+1) >= max_len):
                mass_o.append(mass_user[ind])
                continue
            count = mass_user[ind]
            mass_o.append ( mass_user[ind + 1] )
            mass_o.append ( count )

    return mass_o

def print_mass(mass):
    for i in mass:
        print(i, end=' ')
    print()

mass_out = []
mass = ['1', '2', '3', '4', '5','6']
mass=in_mass()
print_mass(rev_el ( mass, mass_out ))

print_mass(mass)

