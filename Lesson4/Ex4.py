"""
Задание 4.

Приведены два алгоритма. В них определяется число,
которое встречается в массиве чаще всего.

Сделайте профилировку каждого алгоритма через timeit

Попытайтесь написать третью версию, которая будет самой быстрой.
Сделайте замеры и опишите, получилось ли у вас ускорить задачу.
"""
import timeit
import cProfile

array = [1, 3, 1, 3, 4, 5, 1]


def func_1():
    m = 0
    num = 0
    for i in array:
        count = array.count(i)
        if count > m:
            m = count
            num = i
    return f'Чаще всего встречается число {num}, ' \
           f'оно появилось в массиве {m} раз(а)'


def func_2():
    new_array = []
    for el in array:
        count2 = array.count(el)
        new_array.append(count2)

    max_2 = max(new_array)
    elem = array[new_array.index(max_2)]
    return f'Чаще всего встречается число {elem}, ' \
           f'оно появилось в массиве {max_2} раз(а)'


def func_3():
    max_el = sorted([(i, array.count(i)) for i in set(array)], key=lambda t: t[1])[-1]
    return f'Чаще всего встречается число {max_el[0]}, ' \
           f'оно появилось в массиве {max_el[1]} раз(а)'


def func_4():
    d = {}
    for el in array:
        chk = d.get(el)
        if chk is None:
            d[el] = 1
        else:
            d[el] = chk + 1
    sort_d = sorted(d, key=d.__getitem__)
    return f'Чаще всего встречается число {sort_d[len(sort_d) - 1]}, ' \
           f'оно появилось в массиве {d[sort_d[len(sort_d) - 1]]} раз(а)'


print(func_1())
print(func_2())
print(func_3())
print(func_4())
print(timeit.timeit("func_1()", setup="from __main__ import func_1", number=10000))
print(timeit.timeit("func_2()", setup="from __main__ import func_2", number=10000))
print(timeit.timeit("func_3()", setup="from __main__ import func_3", number=10000))
print(timeit.timeit("func_4()", setup="from __main__ import func_4", number=10000))
cProfile.run("func_1()")
cProfile.run("func_2()")
cProfile.run("func_3()")
cProfile.run("func_4()")

'''
Из начальных вариантов самым эффективным является первый - так как выполняем всего один проход по списку и функцию count
Попробовал через генератор списка и через словарь. 
Выиграша в скорости либо нет вовсе либо между первой и второй реализацией
'''