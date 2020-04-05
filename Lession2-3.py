def month_list():
    mon=['январь','февраль','март','апрель','май','июнь','июль', 'август', 'сентябрь', 'октябрь', 'ноябрь', 'декабрь']
    mon_count=['1','2','3','4','5','6','7','8','9','10','11','12']
    dekad=['зима','весна','лето','осень']
    user_input='1'
    while user_input in mon_count:
        user_input= input('Ведите месяц года в числовом выражении. Для выхода наберите больше 12:  ')
        if mon_count.count(user_input)!=0:
            dek=(0 if (int(user_input)<=2) else (1 if (int(user_input)<=5) else (2 if (int(user_input)<=8) else (3 if (int(user_input)<=11) else 0))))
            print(f'Месяц года: {mon[int(user_input)-1]}. Это {dekad[dek]}')

def mon_dekad_slov():
    mon ={'1':'январь','2':'февраль','3':'март','4':'апрель','5':'май','6':'июнь','7':'июль','8': 'август', '9':'сентябрь','10': 'октябрь', '11':'ноябрь', '12':'декабрь'}
    mon_count={'1':'зима','2':'зима','3':'весна','4':'весна','5':'весна','6':'лето','7':'лето','8':'лето','9':'осень','10':'осень','11':'осень','12':'зима'}
    user_input='1'
    while user_input in mon.keys():
        user_input= input('Ведите месяц года в числовом выражении. Для выхода наберите больше 12:  ')
        print(f'Месяц года: {mon.get(user_input)}. Это {mon_count.get(user_input)}. ')





#month_list()
mon_dekad_slov()