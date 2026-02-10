# Торговый автомат
from itertools import count

cost = int(input("Введите стоимость товара: "))

coins = {
    50: 0,
    10: 0,
    5: 0,
    2: 0,
    1: 0
}

for coin in coins:
    coins[coin] = cost // coin
    cost %= coin

for coin, count in coins.items():
    if count > 0:
        print(f"Внесите монеты номиналом {coin}: {count}")

# Квадрат нечетных чисел

numbers = [4, 9, 1, 7, 2, 5, 0, 3, 7, 1, 3]

print("Изначальный список:", numbers)

for i in range(len(numbers)):
    if numbers[i] % 2 == 1:
        numbers[i] = numbers[i] * numbers[i]

print("Измененный список:", numbers)