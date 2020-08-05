import hashlib

"""
Задание 2.
Ваша программа должна запрашивать пароль
Для этого пароля вам нужно получить хеш, используя функцию sha256
Для генерации хеша обязательно нужно использовать криптографическую соль
Обязательно выведите созданный хеш

Далее программа должна запросить пароль повторно
Вам нужно проверить, совпадает ли пароль с исходным
Для проверки необходимо сравнить хеши паролей

ПРИМЕР:
Введите пароль: 123
В базе данных хранится строка: 555a3581d37993843efd4eba1921f1dcaeeafeb855965535d77c55782349444b
Введите пароль еще раз для проверки: 123
Вы ввели правильный пароль
"""

salt = hex(123456)  # по хорошему в целовой среде тут должен быть уникальный ID обращающегося пользователя.
user_pass = input("Введите пароль: ")
res = hashlib.sha256(salt.encode() + user_pass.encode()).hexdigest() + ':' + salt
print("В базе данных хранится строка:", res)
user_pass = input("Введите пароль еще раз для проверки: ")
res2 = hashlib.sha256(salt.encode() + user_pass.encode()).hexdigest() + ':' + salt
if res == res2:
    print("Вы ввели правильный пароль")
else:
    print("Вы ввели неверный пароль")