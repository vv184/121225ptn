#     Извлечение дат
# Реализуйте программу, которая должна:
#     Найти в тексте все даты в форматах DD/MM/YYYY, DD-MM-YYYY и DD.MM.YYYY.


import re

text = "The events N 123456 happened on 15/03/2025, 01.12.2024 and 09-09-2023. Deadline: 28/02/2022."

result = re.findall(r'\d{2}[./-]\d{2}[./-]\d{4}', text)

for date in result:
    print(date)


#     Разделение списка тегов
# Реализуйте программу, которая должна:
#     Прочитать строку с тегами, введёнными пользователем.
#     Разделить её на отдельные теги, независимо от того, чем они были разделены (запятые, точки с запятой, слэши или пробелы).
#     Удалить лишние пробелы и пустые значения.


import re

tag_input = "python, data-science / machine-learning; AI neural-networks"

tags = [tag for tag in re.split(r'[,;/\s]+', tag_input) if tag]

print(tags)