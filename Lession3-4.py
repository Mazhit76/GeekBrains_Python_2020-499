"""
Программа принимает действительное положительное число x и целое отрицательное число y.
Необходимо выполнить возведение числа x в степень y. Задание необходимо реализовать в виде функции my_func(x, y).
При решении задания необходимо обойтись без встроенной функции возведения числа в степень.
Подсказка: попробуйте решить задачу двумя способами.
Первый — возведение в степень с помощью оператора **.
Второй — более сложная реализация без оператора **, предусматривающая использование цикла.
"""

#Функция принимает действительное положительное число x и целое отрицательное или положительное число y
#возводит первое числое в степень второго. Реаливано 2 вида возведеня в степень с поожительным и отрицательным вторым
#числом. Как правильно считает при отрицательном первом числе не проверялось.
def my_func(x,y):
    z=abs(y)
    f=x
    if y<0:
        f=1/abs(y)
    #summa=x**(f)# Первый способ
    #Второй способ
    #Решение взято с сайта https://habr.com/ru/post/469735/ на Си
        num=x
        rootDegree=abs(y)
        eps = 0.00001           #допустимая погрешность
        root = num / rootDegree  #начальное приближение корня
        rn = num                 #значение корня последовательным делением
        countiter = 0               #число итераций
        while (abs(root - rn)>= eps):
            rn = num
            for i in range(1,rootDegree):
                rn = rn / root
            root = 0.5 * ( rn + root)
            countiter=countiter+1
        x=root
    else:
        for i in range(1,y):
            x=x*f

    return x





print(my_func(-9,-3))