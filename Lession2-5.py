def in_mass(mass=[]):
    print ( "Окончание заполнений массива 'None'" )
    user_input = ''
    i=0
    el=0
    while user_input != 'None':
        user_input = input ( 'Введите значение элемента массива:' )
        if (user_input == '') or (user_input == 'None'):
            continue
        user_input = int ( user_input )
        if len(mass)==0:
            mass.insert(0, user_input)
        else:
            for i, el in enumerate ( mass ):
                if el >= user_input:
                    continue
                else:
                    mass.insert ( i+1, user_input )
                break



    return mass

def print_mas(massiv):
    for i in massiv:
        print (i)
mass = []
in_mass (mass)
print_mas(mass)

