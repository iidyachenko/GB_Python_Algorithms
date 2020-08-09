"""
Задание 2.

Приведен код, который формирует из введенного числа
обратное по порядку входящих в него цифр.
Задача решена через рекурсию

Сделайте замеры времени выполнения кода с помощью модуля timeit

Попробуйте оптимизировать код, чтобы снизить время выполнения
Проведите повторные замеры

Подсказка: примените мемоизацию

Добавьте аналитику: что вы сделали и почему
"""
import timeit


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


num = 123445678912345

'''При единочном прогоне мемоизация только замедляет вне зависимости от длины числа, что понятно лишние действия'''
print(timeit.timeit(f"recursive_reverse({num})", setup="from __main__ import recursive_reverse", number=1))
print(timeit.timeit(''f"recursive_reverse_memo({num})", setup="from __main__ import recursive_reverse_memo", number=1))
'''Однако если прогонять функцию много раз то скорость возрастает в разы.
Это результат того что вместо рекурсии значения извлекаются из словаря'''
print(timeit.timeit(f"recursive_reverse({num})", setup="from __main__ import recursive_reverse", number=1000))
print(timeit.timeit(f"recursive_reverse_memo({num})", setup="from __main__ import recursive_reverse_memo", number=1000))
print(recursive_reverse(num))
print(recursive_reverse_memo(num))
