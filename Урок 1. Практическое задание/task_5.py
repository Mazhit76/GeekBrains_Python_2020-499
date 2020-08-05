"""
Задание 5.
Задание на закрепление навыков работы со стеком

Примечание: в этом задании вспомните ваши знания по работе с ООП
и опирайтесь на пример урока

Реализуйте структуру "стопка тарелок".

Мы можем складывать тарелки в стопку и при превышении некоторого значения
нужно начать складывать тарелки в новую стопку.

Структура должна предусматривать наличие нескольких стеков.
Создание нового стека происходит при достижении предыдущим стеком порогового значения.
Реализуйте по аналогии с примером, рассмотренным на уроке, необходимые методы,
для реализации это структуры, добавьте новые методы (не рассмотренные в примере с урока)
для реализации этой задачи.

После реализации структуры, проверьте ее работу на различных сценариях
"""

class PlateStackClass:
    def __init__(self, max_size):
        self.elems=[[]]
        self.max_size= max_size # max size stack
    def __str__(self):
        return str(self.elems)
    def is_empty(self):
        return self.elems == [[]]
#"""Предпологаем, что верхний элемент стека находится в конце списка , если размер равен макс, то создается новая стопка
 #   и туда помещается значение"""

    def push_in(self,el):
        if len(self.elems[len(self.elems)-1])<self.max_size:
            self.elems[len(self.elems)-1].append(el)
        else:
            self.elems.append([])
            self.elems[len(self.elems)-1].append(el)

#"""Берем тарелку из крайней , если она пустая удаляем ее"""

    def pop_out(self):
        result=self.elems[len(self.elems)-1].pop()
        if len(self.elems[len(self.elems)-1])== 0:
            self.elems.pop()
        return result
    def get_val(self):
        return self.elems[len(self.elems)-1][len(self.elems[len(self.elems)-1])-1]
    def stack_size(self):# Общее клоичество тарелок
        elem_sum=0
        for stack in self.elems:
            elem_sum+=len(stack)
        return elem_sum
    def stack_count(self):#Количество стоек
        return len(self.elems)

if __name__== '__main__':
    plates=PlateStackClass(3)
    plates.push_in('Plate1')
    plates.push_in('Plate5')
    plates.push_in('Plate4')
    plates.push_in('Plate5')
    plates.push_in('Plate6')
    print(plates.pop_out())
    print(plates.get_val())
    print(plates.stack_size())
    print(plates.stack_count())
    print(plates)