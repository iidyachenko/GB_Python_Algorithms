"""
Задание 3.

Приведен код, формирующий из введенного числа
обратное по порядку входящих в него
цифр и вывести на экран.

Сделайте профилировку каждого алгоритма через cProfile и через timeit

Сделайте вывод, какая из трех реализаций эффективнее и почему
"""
import timeit
import cProfile


def revers(enter_num, revers_num=0):
    if enter_num == 0:
        return ''
    else:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
        return str(num) + revers(enter_num, revers_num)


def revers_2(enter_num, revers_num=0):
    while enter_num != 0:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
    return revers_num


def revers_3(enter_num):
    enter_num = str(enter_num)
    revers_num = enter_num[::-1]
    return revers_num


print(revers(12345))
print(revers_2(12345))
print(revers_3(12345))

print(timeit.timeit(f"revers({12345})", setup="from __main__ import revers", number=1000))
print(timeit.timeit(f"revers_2({12345})", setup="from __main__ import revers_2", number=1000))
print(timeit.timeit(f"revers_3({12345})", setup="from __main__ import revers_3", number=1000))

cProfile.run(f'revers({1234567891234567891234566666666666666666666665555555555555555555555})')
cProfile.run(f'revers_2({1234567891234567891234566666666666666666666665555555555555555555555})')
cProfile.run(f'revers_3({1234567891234567891234566666666666666666666665555555555555555555555})')

"""
1. Исправил ошибку в 1 функции иначе она не возвращала данные
2. Профилирование для второй и третьей функцией показывает одинаковый результат так как они очень простые 
и быстро выполняются, однако если замерять время то видно что функция 3 выполянется намногобыстрее, 
это связано с тем, что вместо цикла и выполнения операций выполется только переконвертация в строку 
и вывод в обратном порядке
4. Самая медленная это функция с рекурсией это видно как по таймеру так и по проилированию где видно, что функция
выполняется по разу за каждую цифру в числе.
"""