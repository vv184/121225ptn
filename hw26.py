#     Список файлов и папок
# Напишите программу, которая принимает путь к директории через аргумент командной строки и выводит:
#     Отдельно список папок
#     Отдельно список файлов
# Пример запуска
# python script.py /home/user/documents
# Пример вывода
# Содержимое директории '/home/user/documents':
# Папки:
# - folder1
# - folder2
# Файлы:
# - file1.txt
# - file2.txt
# - notes.docx

import os

directory = input("Введите путь к директории: ")

if not os.path.isdir(directory):
    print("Указанный путь не является директорией.")
else:
    folders = []
    files = []

    for item in os.listdir(directory):
        full_path = os.path.join(directory, item)

        if os.path.isdir(full_path):
            folders.append(item)
        elif os.path.isfile(full_path):
            files.append(item)

    print(f"\nСодержимое директории '{directory}':")

    print("\nПапки:")
    for folder in folders:
        print("-", folder)

    print("\nФайлы:")
    for file in files:
        print("-", file)


#     Поиск и удаление файлов с указанным расширением
# Напишите программу, которая:
#     Принимает путь к директории и расширение файлов через аргумент командной строки.
#     Рекурсивно ищет файлы с этим расширением во всех вложенных папках.
#     Спрашивает у пользователя, хочет ли он удалить найденные файлы.
#     Если пользователь подтверждает, удаляет их.
# Пример запуска:
# python script.py /home/user/PycharmProjects/project1 .log
# Пример вывода
# Найдены файлы с расширением '.log':
# - logs/error.log
# - logs/system.log
# - logs/backup/old.log
# - logs/backup/debug.log
# Вы хотите удалить эти файлы? (y/n): y
# Удаление завершено.


import os

directory = input("Введите путь к директории: ")
extension = input("Введите расширение файлов (например .log): ")

if not os.path.isdir(directory):
    print("Указанный путь не является директорией.")
else:
    found_files = []

    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(extension):
                full_path = os.path.join(root, file)
                found_files.append(full_path)

    if not found_files:
        print(f"Файлы с расширением '{extension}' не найдены.")
    else:
        print(f"\nНайдены файлы с расширением '{extension}':")

        for file in found_files:
            print("-", os.path.relpath(file, directory))

        answer = input("\nВы хотите удалить эти файлы? (y/n): ")

        if answer.lower() == "y":
            for file in found_files:
                os.remove(file)

            print("Удаление завершено.")
        else:
            print("Удаление отменено.")