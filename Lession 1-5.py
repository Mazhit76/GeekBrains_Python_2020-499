receipt = int ( input ( 'Введите выручку организации: ' ) )
cost = int ( input ( 'Введите затраты организации: ' ) )

profit = receipt - cost
if profit <= 0:
    print ( f
    'К сожалению ваша организация убыточна и сработала с результатом: {profit} рублей')
    else:
    margin = (cost / receipt) * 100
    print ( f
    'Ваша организация с сработала с прибылью: {profit} рублей. Рентабельность составила {"%.0f"%(margin)} процентов')
    numb_staff = int ( input ( 'Введите количество сотрудников организации: ' ) )
    profit_on_staff = profit / numb_staff
    print ( f
    'Рентабельность на одного сотрудника составила:{"%.0f"%(profit_on_staff)} рублей')
