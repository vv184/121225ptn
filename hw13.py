#     Прогрессия увеличения
# Напишите программу, которая создаёт новый кортеж, состоящий из элементов изначального в том же порядке. Добавить в него только элементы, которые больше всех предыдущих значений в исходном кортеже.
# Данные:
# numbers = (3, 7, 2, 8, 5, 10, 1)
# Пример вывода:
# Кортеж по возрастанию: (3, 7, 8, 10)


numbers = (3, 7, 2, 8, 5, 10, 1)

result = []
current_max = numbers[0]

for num in numbers:
    if num >= current_max and (len(result) == 0 or num > result[-1]):
        result.append(num)
        current_max = num

print("Кортеж по возрастанию:", tuple(result))



#     Повторяющиеся элементы
# Напишите программу, которая находит индексы элементов кортежа, встречающихся более одного раза. Вывести сами элементы и их индексы.
# Данные:
# numbers = (1, 2, 3, 4, 2, 5, 3, 6, 4, 2, 9)
# Пример вывода:
# Индексы элемента 2: 1 4 9
# Индексы элемента 3: 2 6
# Индексы элемента 4: 3 8


numbers = (1, 2, 3, 4, 2, 5, 3, 6, 4, 2, 9)

for i in range(len(numbers)):
    if numbers.count(numbers[i]) > 1:

        already_done = False
        for j in range(i):
            if numbers[j] == numbers[i]:
                already_done = True
                break

        if already_done:
            continue

        print(f"Индексы элемента {numbers[i]}:", end=" ")

        for k in range(len(numbers)):
            if numbers[k] == numbers[i]:
                print(k, end=" ")

        print()