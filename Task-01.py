# Задача 1. Иконки

import os


def check(path):
    if not os.path.exists(os.path.abspath(path)):
        print('Такого файла не существует.')
    else:
        if os.path.isdir(os.path.abspath(path)):
            print('Указанный путь является каталогом.')
        elif os.path.isfile(os.path.abspath(path)):
            print('Указанный путь является файлом.')
            print(f'Размер:{os.path.getsize(os.path.abspath(path))} байт')
        elif os.path.islink(os.path.abspath(path)):
            print('Файл является ссылкой.')


user_enter = input('Путь: ')
check(user_enter)
