"""
3)	Реализовать базовый класс Worker (работник), в котором определить атрибуты: name, surname, position (должность),
 income (доход). Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы: оклад и премия,
  например, {"wage": wage, "bonus": bonus}. Создать класс Position (должность) на базе класса Worker.
   В классе Position реализовать методы получения полного имени сотрудника (get_full_name) и дохода с учетом премии
   (get_total_income). Проверить работу примера на реальных данных (создать экземпляры класса Position, передать данные,
    проверить значения атрибутов, вызвать методы экземпляров).
"""
class Worker:
    def __init__(self, name, surname, positon,wage,bonus):
        self.name=name
        self.surname=surname
        self.position=positon
        self._income={"wage":wage,'bonus':bonus}


class Position(Worker):
   # def __init__(self, name, surname, positon,income, wage,bonus):
     #   super().__init__(name, surname, positon,income, wage,bonus)

    def get_full_name(self):
        print(name,' ', surname,', должность: ', position)
    def get_total_income(self):
        summa= self._income['wage']+self._income['bonus']
        print(f'Доход с учетом премии: {summa}')




name=input('Введите имя сотрудника: ')
surname=input('Введите фамилию сотрудника: ')
position=input('Введите должность сотрудника: ')
wage=int(input('Введите оклад сотрудника: '))
bonus=int(input('Введите премию сотрудника: '))

a=Position(name,surname,position,wage,bonus)

print(a.name)
print(a.surname)
print(a.position)
print(a._income)

a.get_full_name()
a.get_total_income()