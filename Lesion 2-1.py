def in_mass(mass):
    print ( "Окончание заполнений массива '999'" )
    user_input = ''
    while user_input != '999':
        user_input = input ( 'Введите значение элемента массива:' )
        user_type = type ( user_input )
        if user_input == '':
            continue
        elif type ( user_input ) == int:
            mass.append ( int ( user_input ) )
        elif type ( user_input ) == 'str':
            mass.append ( str ( user_input ) )
        elif type ( user_input ) == 'float':
            mass.append ( float ( user_input ) )
        elif type ( user_input ) == 'bool':
            mass.append ( bool ( user_input ) )
        elif type ( user_input ) == 'list':
            mass.append ( list ( user_input ) )
        elif type ( user_input ) == 'turple':
            mass.append ( tuple ( user_input ) )
        elif type ( user_input ) == 'dict':
            mass.append ( dict ( user_input ) )


mass = []
in_mass ( mass )
