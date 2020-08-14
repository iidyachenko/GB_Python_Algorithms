"""
Сравнение производительности очередей и списков
"""
from collections import deque
import timeit


def deq_test():
    string = 'qwe asd zxc'
    deq_obj = deque(list(string.split()))
    deq_obj.append('123')
    deq_obj.appendleft('456')
    deq_obj.rotate(1)
    for el in deq_obj:
        el += el


def list_test():
    string = 'qwe asd zxc'
    list_obj = list(string.split())
    list_obj.append('123')
    list_obj.insert(0, '456')
    list_obj.insert(0, list_obj[len(list_obj)-1])
    list_obj.pop()
    for el in list_obj:
        el += el


print(timeit.timeit(f"deq_test()", setup="from __main__ import deq_test", number=10000))
print(timeit.timeit(f"list_test()", setup="from __main__ import list_test", number=10000))

"""
Разницы между списком и оередью по поизводительностью на маленьких объемов практически нет.
Однако очередь будет чуть быстрее если часто применять функции свойсвенные толко для очереди 
"""