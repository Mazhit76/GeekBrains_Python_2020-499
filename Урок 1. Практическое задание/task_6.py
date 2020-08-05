"""
Задание 6.
Задание на закрепление навыков работы с очередью

Примечание: в этом задании вспомните ваши знания по работе с ООП
и опирайтесь на пример урока

Реализуйте структуру "доска задач".


Структура должна предусматривать наличие несольких очередей задач, например
1) базовой, откуда задачи берутся, решаются и отправляются в список решенных
2) очередь на доработку, когда нерешенные задачи из первой очереди отправляются
на корректировку решения

После реализации структуры, проверьте ее работу на различных сценариях
"""

class QueueClass:
    def __init__(self):
        self.elems=[]
    def is_empty(self):
        return self.elems==[]
    def to_queue(self, item):
        self.elems.insert(0,item)
    def from_queue(self):
        return self.elems.pop()
    def size(self):
        return len(self.elems)
class TaskBoard:
    def __init__(self):
        self.cur_cueue =QueueClass()# Base len
        self.revisin_queue =QueueClass() # Go work len
        self.log=[] # len good work
    def resolve_task(self):
        task=self.cur_cueue.from_queue()# take work from len and give to do
        self.revisin_queue.to_queue(task)
    def to_revision_task(self):
        task=self.cur_cueue.from_queue()# send to work is time
        self.cur_cueue.to_queue(task)
    def to_curent_cueue(self,item):
        self.cur_cueue.to_queue(item)# add to workt current time
    def from_revision(self):
        task= self.revisin_queue.from_queue()# return from work in current queue
        self.cur_cueue.to_queue(task)
    def curent_task(self):
        return self.cur_cueue.elems[len(self.cur_cueue.elems)-1]# current task
    def current_revision(self):
        return  self.revisin_queue.elems[len(self.revisin_queue.elems)-1] # task in work




