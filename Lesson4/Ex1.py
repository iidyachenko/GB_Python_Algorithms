import timeit

"""
Задание 1.

Приведен код, который позволяет сохранить в
массиве индексы четных элементов другого массива

Сделайте замеры времени выполнения кода с помощью модуля timeit

Попробуйте оптимизировать код, чтобы снизить время выполнения
Проведите повторные замеры

Добавьте аналитику: что вы сделали и почему
"""


def func_1(nums):
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr


def func_2(nums):
    return [i for i in range(len(nums)) if nums[i] % 2 == 0]


def func_3(nums):
    new_arr = []
    i = 0
    for el in nums:
        if el % 2 == 0:
            new_arr.append(i)
            i += 1
    return new_arr


old_nums = [i for i in range(1, 100)]
print(func_3(old_nums))

print(timeit.timeit(f"func_1({old_nums})", setup="from __main__ import func_1", number=1000))
print(timeit.timeit(f"func_2({old_nums})", setup="from __main__ import func_2", number=1000))
print(timeit.timeit(f"func_3({old_nums})", setup="from __main__ import func_3", number=1000))

""" 
Заменил на генератор списка, получил небольшой прирост. 
В третьей функции использовал последовательный перебор без обраения по индексы, выигрыш в скорости еще меньше но есть
"""