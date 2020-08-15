"""
Задание 1.
Выполните профилирование памяти в скриптах
Проанализировать результат и определить программы с
наиболее эффективным использованием памяти.

Примечание: Для анализа возьмите любые 1-3 ваших программы или несколько
вариантов кода для одной и той же задачи. Можно взять задачи с курса Основ или с текущего курса Алгоритмов

Результаты анализа вставьте в виде комментариев к коду.
Также укажите в комментариях версию Python и разрядность вашей ОС.

ВНИМАНИЕ: ЗАДАНИЯ, В КОТОРЫХ БУДУТ ГОЛЫЕ ЦИФРЫ ЗАМЕРОВ (БЕЗ АНАЛИТИКИ)
БУДУТ ПРИНИМАТЬСЯ С ОЦЕНКОЙ УДОВЛЕТВОРИТЕЛЬНО

ЧАСТЬ 1. Упражнение по созданию класа рабочего взято с основ Python
ОС: Windows 10 64-x
Версия Python: 3.8.5
"""
from random import randint
from memory_profiler import profile
from pympler import asizeof


# Создаем обычный класс рабочего и его потомка.
class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self.income = {"wage": int(wage), "bonus": int(bonus)}


class Position(Worker):
    def __init__(self, name, surname, position, wage, bonus):
        super().__init__(name, surname, position, wage, bonus)

    def get_full_name(self):
        return self.name + " " + self.surname

    def get_total_income(self):
        return self.income["wage"] + self.income["bonus"]


# Создаем класс рабочего и его потомка со слотами.
class WorkerSlot:
    __slots__ = ['name', 'surname', 'position', 'income']

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self.income = {"wage": int(wage), "bonus": int(bonus)}


class PositionSlot(Worker):
    __slots__ = ['name', 'surname', 'position', 'income']

    def __init__(self, name, surname, position, wage, bonus):
        super().__init__(name, surname, position, wage, bonus)

    def get_full_name(self):
        return self.name + " " + self.surname

    def get_total_income(self):
        return self.income["wage"] + self.income["bonus"]


@profile
def create_worker_list(worker, count):
    """Создаем массив из уазанных рабочих"""
    worker_list = []
    for i in range(1, count):
        worker_new = Position(worker.name + str(i), worker.surname + str(i), worker.position, randint(100, 200),
                              randint(100, 200))
        worker_list.append(worker_new)
    return worker_list


worker_ivan = Position("Ivan", "Ivanov", "Worker", 100, 200)
print('Рабочий без слота: ', asizeof.asizeof(worker_ivan))
worker_ivan_slot = PositionSlot("Ivan", "Ivanov", "Worker", 100, 200)
print('Рабочий со слотами: ', asizeof.asizeof(worker_ivan_slot))
create_worker_list(worker_ivan_slot, 10000)
create_worker_list(worker_ivan, 10000)

"""
Анализ
Использовал два способа создания объекта класса: Стандартным способом и через слоты
Объект с использованием слота весит меньше: 424 против 544
Однако при создании большоего количества объектов разницы уже нет, возможно сказывается повторяймост ссылок
Результат профилирования выполнения функци создания 10000 обектов без слотов:
Line #    Mem usage    Increment   Line Contents
================================================
    69     22.7 MiB     22.7 MiB   @profile
    70                             def create_worker_list(worker, count):
    71                                 "Создаем массив из уазанных рабочих"
    72     22.7 MiB      0.0 MiB       worker_list = []
    73     25.6 MiB      0.0 MiB       for i in range(1, count):
    74     25.6 MiB      0.1 MiB           worker_new = Position(worker.name + str(i), worker.surname + str(i), worker.position, randint(100, 200),
    75     25.6 MiB      0.0 MiB                                 randint(100, 200))
    76     25.6 MiB      0.0 MiB           worker_list.append(worker_new)
    77     25.6 MiB      0.0 MiB       return worker_list


Со слотами:
Line #    Mem usage    Increment   Line Contents
================================================
    69     22.7 MiB     22.7 MiB   @profile
    70                             def create_worker_list(worker, count):
    71                                 "Создаем массив из уазанных рабочих"
    72     22.7 MiB      0.0 MiB       worker_list = []
    73     25.6 MiB      0.0 MiB       for i in range(1, count):
    74     25.6 MiB      0.1 MiB           worker_new = Position(worker.name + str(i), worker.surname + str(i), worker.position, randint(100, 200),
    75     25.6 MiB      0.0 MiB                                 randint(100, 200))
    76     25.6 MiB      0.0 MiB           worker_list.append(worker_new)
    77     25.6 MiB      0.0 MiB       return worker_list


"""
