import hashlib
"""
Задание 4.
Реализуйте скрипт "Кэширование веб-страниц"

Функция должна принимать url-адрес и проверять
есть ли в кэше соответствующая страница, если нет, то вносит ее в кэш

Подсказка: задачу решите обязательно с применением 'соленого' хеширования
Можете условжнить задачу, реализовав ее через ООП
"""
urls = {}
while True:
    user_url = input("Введите URL:")
    salt = hashlib.sha256(user_url[len(user_url)-3:len(user_url)].encode()).hexdigest()
    hash_url = hashlib.sha256(user_url.encode()).hexdigest() + salt
    if urls.get(hash_url) is None:
        urls[hash_url] = salt
        print("URL добавлен в кэш")
    else:
        print("Такой URL уже есть")
    if input("Продолжим ввод? y/n") == 'n':
        break

