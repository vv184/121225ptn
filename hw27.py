#     Фильтрация по ключевому слову
# Напишите программу, которая ищет в файле все строки, содержащие указанное пользователем слово, и сохраняет их в новый файл.
#     Имя нового файла формируется как <keyword>_<original_filename>.
#     Если файл не существует, программа должна вывести ошибку.
#     Если совпадения не найдены, новый файл не создаётся.
# Используйте файл system_log.txt.
# Пример ввода:
# Введите имя файла для поиска: system_log.txt
# Введите ключевое слово: error
# Пример вывода:
# Строки, содержащие 'error', сохранены в error_system_log.txt.

filename = input("Введите имя файла для поиска: ")
keyword = input("Введите ключевое слово: ").lower()

try:
    with open(filename, "r", encoding="utf-8") as file:
        lines = file.readlines()

    matching_lines = [line for line in lines if keyword in line.lower()]

    if matching_lines:
        new_filename = f"{keyword}_{filename}"

        with open(new_filename, "w", encoding="utf-8") as new_file:
            new_file.writelines(matching_lines)

        print(f"Строки, содержащие '{keyword}', сохранены в {new_filename}.")
    else:
        print(f"Совпадений по слову '{keyword}' не найдено. Файл не создан.")

except FileNotFoundError:
    print("Ошибка: файл не существует.")

#     Поиск и удаление дубликатов
# Напишите программу, которая удаляет дублирующиеся строки из файла и сохраняет результат в новый файл.
#     Имя нового файла формируется как unique_<original_filename>.
#     Если файл не существует, программа должна вывести ошибку.
#     Исходный порядок строк должен сохраниться.
#     Если в файле нет дубликатов, создаётся точная копия файла.
# Используйте файл movies_to_watch.txt.
# Пример ввода:
# Введите имя файла: movies_to_watch.txt
# Пример вывода:
# Дубликаты удалены. Уникальные строки сохранены в unique_movies_to_watch.txt.

filename = input("Введите имя файла: ")

try:
    with open(filename, "r", encoding="utf-8") as file:
        lines = file.readlines()

    unique_lines = []
    seen = set()

    for line in lines:
        if line not in seen:
            unique_lines.append(line)
            seen.add(line)

    new_filename = f"unique_{filename}"

    with open(new_filename, "w", encoding="utf-8") as new_file:
        new_file.writelines(unique_lines)

    print(f"Дубликаты удалены. Уникальные строки сохранены в {new_filename}.")
except FileNotFoundError:
    print("Ошибка: файл не существует.")