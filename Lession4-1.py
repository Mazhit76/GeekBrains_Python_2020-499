"""
Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
 В расчете необходимо использовать формулу: (выработка в часах * ставка в час) + премия.
 Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.
 """
 # Вызвали библиотекой другую функцию предваритеотно в Parameters/Edit configurtionas/Run подставив 3 параметра через пробел
from main import payrol
summa,production,rate,prize=payrol()
print(f'{production}часов-выработка,'
      f' {rate}-ставка, рублей в час,  '
      f'{prize} рублей-премия. Итого: {summa} рублей')