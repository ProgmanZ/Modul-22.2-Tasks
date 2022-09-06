# Второй вариант решения задачи

import os


def search(file_path, file_name):

    for element in os.listdir(file_path):
        full_path = os.path.join(file_path, element)

        if element == file_name:
            return os.path.join(full_path, file_name)

        if os.path.isdir(full_path):
            result = search(full_path, file_name)

            if result:
                break

    else:
        result = None

    return result


user_path = input('Где ищем: ')
user_file = input('Файл для поиска: ')
print(search(os.path.abspath(user_path), user_file))
