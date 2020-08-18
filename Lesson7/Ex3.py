"""
3. Массив размером 2m + 1, где m – натуральное число, заполнен случайным образом.
Найдите в массиве медиану. Медианой называется элемент ряда, делящий его на
две равные части: в одной находятся элементы, которые не меньше медианы,
в другой – не больше медианы.

Задачу можно решить без сортировки исходного
массива.

Но если это слишком сложно, то используйте метод сортировки,
который не рассматривался на уроках: Шелла, Гномья, ...

arr[m]
from statistics import median
"""
from statistics import median
import random
import timeit


def my_median(array):
    """Решение без сортировки"""
    for i in array:
        left = 0
        right = 0
        for j in array:
            if i >= j:
                left += 1
            else:
                right += 1
        if left >= len(array)//2 and right == len(array)//2:
            return i


def gnome_sort(array):
    """Решение с гномьей сортировкой"""
    i = 1
    j = 2
    while i < len(array):
        if array[i-1] > array[i]:
            i = j
            j += 1
        else:
            array[i-1], array[i] = array[i], array[i-1]
            i = i - 1
            if i == 0:
                i = j
                j = j + 1
    return array


def my_median_sort(array, m):
    gnome_sort(array)
    return array[m]


m = int(input("Введите середину массива: "))
array = [random.randint(-100, 100) for _ in range(2*m + 1)]
print("Начальный массив:", array)
print("Медиана из модуля statistics:", median(array))
print("Медиана из собственного модуля:", my_median(array))
print("Сортируем массив методом гномика:",gnome_sort(array))
print("Выбираем средний элемент, это и будет медиана:", array[m])


"""Решил ради интереса посчитать скорость"""
array_test = [random.randint(-100, 100) for _ in range(2*m + 1)]

print("Встроенная функция медианы:")
print(timeit.timeit(f"median({array_test})",
                    setup="from statistics import median", number=1))

print("Моя функция медианы:")
print(timeit.timeit("my_median(array_test)",
                    setup="from __main__ import my_median, array_test", number=1))

print("Медиана через сортировку:")
print(timeit.timeit(f"my_median_sort(array_test,{m})",
                    setup="from __main__ import my_median_sort, array_test", number=1))

"""Результат
На маленьком масиве самая быстрый результат показывает поиск через сортировку, затем встроенная медиана а пото моя
Однако чем больше массив тем разница меньше, при большом масиве стандартная функция поиска медианы намного быстрее всех"""