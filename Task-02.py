# Задача 2. Поиск файла

import os


def search(user_path, user_file):
    if os.path.isdir(os.path.abspath(user_path)):
        for element in os.listdir(user_path):
            search(os.path.join(os.path.abspath(user_path), element), user_file)
    else:
        if user_path.split(os.sep)[-1] == user_file:
            print(user_path)


usr_path = input('Ищем в: ')
usr_file = input('Имя файла: ')

search(os.path.abspath(usr_path), usr_file)

print('Найдены следующие пути:')
