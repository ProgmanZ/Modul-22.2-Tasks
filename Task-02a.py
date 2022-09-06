# Второй вариант решения задачи от SkillBox
# Правда останавливается при нахождении первого совпадения файла.

import os


def search(file_path, file_name):
    print('Переходим в', file_path)

    for element in os.listdir(file_path):
        full_path = os.path.join(file_path, element)
        print('\tСмотрим', full_path)

        if element == file_name:
            return full_path

        if os.path.isdir(full_path):
            print(full_path.split(os.sep)[-1], 'Это директория')
            result = search(full_path, file_name)
            if result:
                break

    else:
        result = None

    return result


user_path = input('Где ищем: ')
user_file = input('Файл для поиска: ')
print(search(os.path.abspath(user_path), user_file))
