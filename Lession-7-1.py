"""
1)	Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()),
который должен принимать данные (список списков) для формирования матрицы.
Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
Примеры матриц: 3 на 2, 3 на 3, 2 на 4.

31	22
37	43
51	86

3	5	32
2	4	6
-1	64	-8

3	5	8	3
8	3	7	1


Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов класса Matrix
(двух матриц). Результатом сложения должна быть новая матрица.
Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки первой матрицы
складываем с первым элементом первой строки второй матрицы и т.д.


"""


class Matrix:
    def __init__(self, a):
        self.b = '\n'.join(['\t'.join([str(j) for j in i]) for i in a])
        List = []
        for i in a:
            List.append([j for j in i])    # С этим у меня беда прямо, сутки в никуда потратил.Так и не разобрался.
        self.a = List

    def __str__(self):                      # Об это предупреждали. Все понятно.
        self.c = str(self.a)
        return self.c

    def mass_same(m1,m2):                   #Этот костыдь сам засунул, без него некторые значения матриц  откидывет
        max_hight=max(len(m1),len(m2))      #По хорошему его в __add__вставить надо, там он покороче был бы....
        max_len=max(len(m1[0]),len(m2[0]))
        for i in range(len(m1),max_hight):
            m1.append([])
        for i in range(0,max_hight):
            for j in range(len(m1[i]),max_len):
                m1[i].append(0)
        for i in range(len(m2),max_hight):
            m2.append([])
        for i in range(0,max_hight):
            for j in range(len(m2[i]),max_len):
                m2[i].append(0)
        return m1,m2

    def __add__(self, other):# " Это с интренета сдул бессовестно. Код прочитал-менять, боюсь что- то и уже времени нет.
        result = []           # Время будет обратно вернусь, покопаться надо будет.
        numbers = []
        for i in range(len(self.a)):
            for j in range(len(self.a[0])):
                summa = other.a[i][j] + self.a[i][j]
                numbers.append(summa)
                if len(numbers) == len(self.a):
                    result.append(numbers)
                    numbers = []
        return Matrix(result)


mass1=[[31,22],[37,43],[51,86]]
mass2=[[3,5,32],[2,4,6],[-1,64,-8]]
mass3=[[3,5,8,3],[8,3,7,1]]

mass4,mass5=Matrix.mass_same(mass1,mass3)
m1=Matrix(mass4)
m2=Matrix(mass5)
print(m1 + m2)

