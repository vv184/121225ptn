#     Повторения букв
# Реализуйте функцию, которая принимает текст и возвращает словарь
# с подсчётом количества каждой буквы, игнорируя регистр.
# Данные:
# text = "Programming is fun!"
# Пример вывода:
# {'p': 1, 'r': 2, 'o': 1, 'g': 2, 'a': 1, 'm': 2, 'i': 2, 'n': 2, 's': 1, 'f': 1, 'u': 1}

text = "Programming is fun!"

letter_count = {}

for char in text.lower():
    if char.isalpha():
        letter_count[char] = letter_count.get(char, 0) + 1

print(letter_count)

#     Группировка студентов по классам
# Создайте структуру для группировки студентов по классам.
# Добавьте студентов в соответствующие группы.
# Данные:
# students = [("class1", "Alice"), ("class2", "Bob"), ("class1", "Charlie"), ("class3", "Daisy")]
# Пример вывода:
# {'class1': ['Alice', 'Charlie'], 'class2': ['Bob'], 'class3': ['Daisy']}

students = [
    ("class1", "Alice"),
    ("class2", "Bob"),
    ("class1", "Charlie"),
    ("class3", "Daisy")
]

groups = {}

for class_name, student in students:
    groups.setdefault(class_name, []).append(student)

print(groups)