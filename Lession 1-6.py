first_result= int(input('Введите ваш первоначальный результат в километрах : '))
max_result= int(input('Введите вашу цель тренировок в километрах: '))
day=1
procent_strange=10
print(f'Если будете усиленно тренироваться и наращивать каждый результат на {procent_strange}%, то Ваши результаты будут:')
while True:
    print(f'На {day}-ый день, Ваш результат: {"%.2f"%(first_result)}')
    if first_result<max_result:
        first_result=first_result+first_result/procent_strange
        day+=1
    else:
        break