import hashlib

"""
Задание 3.
Определить количество различных подстрок с использованием хеш-функции.
Дана строка S длиной N, состоящая только из строчных латинских букв.

Подсказка: примените хеши и множества

рара:

рар
ра
ар
ара
р
а
"""

string = input("Введите строку: ")
res = set()

for i in range(0, len(string)):
    for j in range(i+1, len(string)+1):
        res.add(hashlib.sha256(string[i:j].encode()).hexdigest())

print("Количество подстрок:", len(res))
