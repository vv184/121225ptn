# Звёздочки вместо чисел

text = "My number is 123-456-789"

result = ""

for x in text:
    if x >= "0" and x <= "9":
        result = result + "*"
    else:
        result = result + x

print("Строка:", text)
print("Результат:", result)

# Количество символов

text = "Programming in Python"

print("Строка:", text)

text = text.lower()

for x in text:
     count = text.count(x)
     if count > 1:
         print("Символ", "'", x, "встречается", count, "раз(а)")
         text = text.replace(x, "")

# Увеличение чисел

text = "I have 5 apples and 10 oranges, price is 0.5 each. Card number is ....3672."

res = ""
num = ""
x = 0
while x < len(text):
    if text[x:x+4] == "....":
        res += "...."
        x += 4
        while x < len(text) and text[x].isdigit():
            res += text[x]
            x += 1
        continue
    c = text[x]
    if c.isdigit() or (c == "." and num):
        num += c
    else:
        if num:
            res += str(float(num) * 10)
            num = ""
        res += c
    x += 1
if num:
    res += str(float(num) * 10)

print(res)

