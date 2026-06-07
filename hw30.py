#     Анализ курсов студентов
# Реализовать программу, которая должна:
#     Прочитать файл student_courses.json, содержащий:
#         имя,
#         дату рождения (birth_date) в формате дд.мм.гггг,
#         дату поступления (enrollment_date) в том же формате,
#         список курсов.
#     Вычислить:
#         Общее количество студентов.
#         Средний возраст на момент поступления.
#         Количество студентов на каждом курсе.
#     Сохранить отчёт в JSON-файл student_courses_report.json.
# Данные:
# [
#   {"name": "Diana Williams", "birth_date": "12.06.1983", "enrollment_date": "29.04.2023", "courses": ["Physics", "Chemistry"]},
#   {"name": "Tina Miller", "birth_date": "06.07.2004", "enrollment_date": "18.04.2020", "courses": ["Biology", "Business"]},
#   {"name": "Kevin Miller", "birth_date": "20.12.2004", "enrollment_date": "16.12.2020", "courses": ["Linguistics", "Math", "History"]},
#   {"name": "Fiona Brown", "birth_date": "05.07.1999", "enrollment_date": "02.09.2022", "courses": ["Art", "Philosophy"]},
#   {"name": "Charlie Davis", "birth_date": "17.07.1998", "enrollment_date": "17.05.2023", "courses": ["Chemistry", "Physics", "Business"]},
#   {"name": "Diana Jones", "birth_date": "24.12.1980", "enrollment_date": "26.11.2021", "courses": ["Economics", "Linguistics"]},
#   {"name": "Alice Johnson", "birth_date": "22.09.1981", "enrollment_date": "23.12.2020", "courses": ["Chemistry", "Economics", "Math"]},
#   {"name": "Ian Lopez", "birth_date": "23.11.2001", "enrollment_date": "07.05.2020", "courses": ["Philosophy", "Art", "Physics"]},
#   {"name": "Kevin Davis", "birth_date": "30.01.1997", "enrollment_date": "20.03.2021", "courses": ["Math", "Economics"]},
#   ...
# ]
# Пример вывода (student_courses_report.json):
# {
#     "total_students": 100,
#     "average_enrollment_age": 27.9,
#     "students_per_course": {
#         "Art": 21,
#         "Biology": 18,
#         "Business": 28,
#         "Chemistry": 16,
#         "Economics": 23,
#         "History": 9,
#         "Linguistics": 23,
#         "Math": 23,
#         "Philosophy": 19,
#         "Physics": 19
#     }
# }


import json
from datetime import datetime
from collections import Counter


DATE_FORMAT = "%d.%m.%Y"


def calculate_age_at_enrollment(birth_date_str, enrollment_date_str):
    birth_date = datetime.strptime(birth_date_str, DATE_FORMAT)
    enrollment_date = datetime.strptime(enrollment_date_str, DATE_FORMAT)

    age = enrollment_date.year - birth_date.year

    if (enrollment_date.month, enrollment_date.day) < (birth_date.month, birth_date.day):
        age -= 1

    return age


def main():
    with open("student_courses.json", "r", encoding="utf-8") as f:
        students = json.load(f)

    total_students = len(students)

    ages = []
    course_counter = Counter()

    for student in students:
        age = calculate_age_at_enrollment(
            student["birth_date"],
            student["enrollment_date"]
        )
        ages.append(age)

        course_counter.update(student["courses"])

    average_enrollment_age = round(sum(ages) / total_students, 1) if total_students else 0

    report = {
        "total_students": total_students,
        "average_enrollment_age": average_enrollment_age,
        "students_per_course": dict(sorted(course_counter.items()))
    }

    print(json.dumps(report, ensure_ascii=False, indent=4))

    with open("student_courses_report.json", "w", encoding="utf-8") as f:
        json.dump(report, f, ensure_ascii=False, indent=4)

    print("Отчёт сохранён в student_courses_report.json")


if __name__ == "__main__":
    main()