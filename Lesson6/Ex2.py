from memory_profiler import profile
from numpy import array
from pympler import asizeof


'''Проанализируем потребление памяти на основе функций переворачивающих цыфры в числе'''


def memorize(func):
    def g(n, memory={}):
        r = memory.get(n)
        if r is None:
            r = func(n)
            memory[n] = r
        return r
    return g


def recursive_reverse(number):
    if number == 0:
        return str(number % 10)
    return f'{str(number % 10)}{recursive_reverse(number // 10)}'


@memorize
def recursive_reverse_memo(number):
    if number == 0:
        return str(number % 10)
    return f'{str(number % 10)}{recursive_reverse_memo(number // 10)}'


@profile
def recurs_stat(fun, number, stat):
    for _ in range(1, stat):
        fun(number)


num = 9999999999**40
# recurs_stat(recursive_reverse, num, 10)
# recurs_stat(recursive_reverse_memo, num, 10)
"""Вначале проверим как работают рекурсии
Как и предпологалось на большом объеме входной строки, функция с использованием мемоизации начинает потреблять
болбше памяти. 
Без мемоизации: 
Line #    Mem usage    Increment   Line Contents
================================================
    30     13.3 MiB     13.3 MiB   @profile
    31                             def recurs_stat(fun, number, stat):
    32     13.6 MiB      0.0 MiB       for _ in range(1, stat):
    33     13.6 MiB      0.3 MiB           fun(number)
    
С мемоизацией:
Line #    Mem usage    Increment   Line Contents
================================================
    30     13.6 MiB     13.6 MiB   @profile
    31                             def recurs_stat(fun, number, stat):
    32     14.0 MiB      0.0 MiB       for _ in range(1, stat):
    33     14.0 MiB      0.4 MiB           fun(number)
"""

"""Теперь попробуем сделать то же самое без рекурсии"""


@profile
def revers_2(enter_num, revers_num=0):
    while enter_num != 0:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
    return revers_num


@profile
def revers_3(enter_num):
    enter_num = str(enter_num)
    revers_num = enter_num[::-1]
    return revers_num


# revers_2(num)
# revers_3(num)

"""
Расход памяти чуть мень чем с обычной рекурсией
Line #    Mem usage    Increment   Line Contents
================================================
    62     13.3 MiB     13.3 MiB   @profile
    63                             def revers_2(enter_num, revers_num=0):
    64     13.3 MiB      0.0 MiB       while enter_num != 0:
    65     13.3 MiB      0.0 MiB           num = enter_num % 10
    66     13.3 MiB      0.0 MiB           revers_num = (revers_num + num / 10) * 10
    67     13.3 MiB      0.0 MiB           enter_num //= 10
    68     13.3 MiB      0.0 MiB       return revers_num


Filename: C:/Users/Игорь/PycharmProjects/GB_Python_Algorithms/Lesson6/Ex2.py

Line #    Mem usage    Increment   Line Contents
================================================
    71     13.3 MiB     13.3 MiB   @profile
    72                             def revers_3(enter_num):
    73     13.3 MiB      0.0 MiB       enter_num = str(enter_num)
    74     13.3 MiB      0.0 MiB       revers_num = enter_num[::-1]
    75     13.3 MiB      0.0 MiB       return revers_num
"""


@profile
def revers_4(enter_num):
    enter_num = str(enter_num)
    new_line = ''
    for i in range(1, len(enter_num) + 1):
        new_line += enter_num[len(enter_num) - i]
    return new_line


def revers_4_generator_list(enter_num):
    for i in range(1, len(enter_num) + 1):
        yield enter_num[len(enter_num) - i]


def revers_4_generator_str(enter_num):
    enter_num = str(enter_num)
    for i in range(1, len(enter_num) + 1):
        yield enter_num[len(enter_num) - i]


@profile
def test_generator(gen):
    for i in gen:
        print(i)


# revers_4(num)
# generator_str = revers_4_generator_str(num)
# generator_list = revers_4_generator_list(list(str(num)))
# test_generator(generator_list)
# test_generator(generator_str)

"""Генераторы как и предпологалось тоже показывают наилучший результат
впрочем как и цикл по строке но наверное все же задача слишком простая
Line #    Mem usage    Increment   Line Contents
================================================
   126     13.2 MiB     13.2 MiB   @profile
   127                             def test_generator(gen):
   128     13.2 MiB      0.0 MiB       for i in gen:
   129     13.2 MiB      0.0 MiB           print(i)
"""


@profile
def num_recur(numbers):
    arr = array(list(str(numbers)))
    return arr[::-1]


print(asizeof.asizeof(array(list(str(num)))))
print(asizeof.asizeof(list(str(num))))
"""numpy тут нет смысла добавлять так как размер вставляемой библиотеки больше выиграша по скорости
Line #    Mem usage    Increment   Line Contents
================================================
   150     22.2 MiB     22.2 MiB   @profile
   151                             def num_recur(numbers):
   152     22.2 MiB      0.0 MiB       arr = array(list(str(numbers)))
   153     22.2 MiB      0.0 MiB       return arr[::-1]

Хотя array будет меньше по размеру чем list 
в нашем примере с очень большим входным числом резульатат был 1648 против 1952
"""

