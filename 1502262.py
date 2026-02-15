# Сумма положительных чисел

numbers = [1245.4435, -302.1403, 87459.99, -520.8265, 1450.001]

s = sum(num for num in numbers if num > 0)
sum = f"${s:,.2f}"
print(f"Сумма положительных чисел: {sum}")

# Счета клиентов

data_list = [
    "John 23 12345.678",
    "Alice 30 200.50",
    "Bob 35 15000.3",
    "Charlie 40 500.75"
]

for x in data_list:
    name, age, balance = x.split()

    age = int(age)
    balance = float(balance)

    print(f"Имя: {name:<8} | Возраст: {age:>2} | Баланс: {balance:>8.2f}")
    