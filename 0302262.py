#Проверка кодировки

a = input("Введите символ: ")

print("Код Unicode:", ord(a))
print("ASCII символ:", ord(a) < 128)

#Подстрока с заполнением

a = input("Введите строку: ")
start = int(input("Введите начальный индекс: "))
end = int(input("Введите конечный индекс: "))

b = a[start:end] + "_" * max(0, end - len(a))
print("Подстрока:", b)

#Подсчёт символа

a = input("Введите строку: ")
b = input("Введите символ: ")
print("Символ", b, "встречается", a.count(b), "раз(а).")

#Инвертирование строки без цифр

a = input("Введите строку: ")
res = ""
for c in a:
    if not c.isdigit():
        res = c + res
print("Результат:", res)

