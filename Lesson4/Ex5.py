"""
Задание 5.*

Приведен наивный алгоритм нахождения i-го по счёту
простого числа (через перебор делителей).

Попробуйте решить эту же задачу,
применив алгоритм "Решето эратосфена" (https://younglinux.info/algorithm/sieve)

Подсказка:
Сравните алгоритмы по времени на разных порядковых номерах чисел:
10, 100, 1000
Опишите результаты, сделайте выводы, где и какой алгоритм эффективнее
Подумайте и по возможности определите сложность каждого алгоритма
"""
import timeit


def simple(i):
    """Без использования «Решета Эратосфена»"""
    count = 1
    n = 2
    while count <= i:
        t = 1
        is_simple = True
        while t <= n:
            if n % t == 0 and t != 1 and t != n:
                is_simple = False
                break
            t += 1
        if is_simple:
            if count == i:
                break
            count += 1
        n += 1
    return n


def gen_primes():
    """Решение через генератор с применением решета"""
    d = {}
    q = 2
    while True:
        if q not in d:
            yield q
            d[q * q] = [q]
        else:
            for p in d[q]:
                d.setdefault(p + q, []).append(p)
            del d[q]
        q += 1


def eratosfen(n):
    gen = gen_primes()
    num = 1
    for _ in range(0, n):
        num = gen.__next__()
    return num


i = int(input('Введите порядковый номер искомого простого числа: '))
print(simple(i))
print(eratosfen(i))
print(timeit.timeit(f"simple({i})", setup="from __main__ import simple", number=10))
print(timeit.timeit(f"eratosfen({i})", setup="from __main__ import eratosfen", number=10))

"""
При большом вводимом чилсе i скорость использования генератора вырастает в разы
На моей машине при 1000 было 4 секунды против 0,05 секунды.
Это связано со сложностью O(n**2) в первом варрианте и nlogn во втором
"""