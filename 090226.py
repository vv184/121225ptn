# Таблица умножения

a = int(input("Введите число: "))
b = len(str(a * a)) + 1

for i in range(1, a + 1):
    for j in range(1, a + 1):
        print(f"{i * j:{b}}", end=" ")
    print()

# Лестница чисел

a = int(input("Введите число: "))

for i in range(1, a + 1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()

# Удаление всех повторяющихся символов

a = input("Введите строку: ")

res = ""
for b in a:
    if b not in res:
        res += b

print("Результат:", res)