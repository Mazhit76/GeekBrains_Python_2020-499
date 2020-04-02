count = list ( input ( 'Введите целое положительное число n: ' ) )
max_count = 0
i = 0
while i < len ( count ):
    if int ( count[i] ) >= max_count:
        max_count = int ( count[i] )
    i = i + 1
print (f' Максимальное число из введенных вами это число: {max_count}')
