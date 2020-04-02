user_sec = int(input('Введите время в секундах: '))
hour = user_sec//3600
minute = user_sec%3600//60
sec = user_sec%3600%60
print(f'{"%.2d"%(hour)}:{"%.2d"%(minute)}:{"%.2d"%(sec)}')


