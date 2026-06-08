#     Банковский счёт
# Создайте класс BankAccount, описывающий банковский счёт.
#     Объект должен хранить имя владельца и текущий баланс.
#     Реализуйте методы:
#         пополнение счёта
#         снятие средств
#         отображение баланса
#     При попытке снять больше, чем есть на счёте, операция не должна выполняться.
# Продумайте, какие поля и методы следует скрыть от внешнего доступа, а какие оставить открытыми.


class BankAccount:
    def __init__(self, owner: str, balance: float = 0):
        self._owner = owner
        self._balance = balance

    def deposit(self, amount: float):
        if amount <= 0:
            print("Error: Amount must be positive.")
            return
        self._balance += amount
        print(f"Current balance: {self._balance}")

    def withdraw(self, amount: float):
        if amount <= 0:
            print("Error: Amount must be positive.")
            return
        if amount > self._balance:
            print("Error: Not enough funds.")
            print(f"Current balance: {self._balance}")
            return
        self._balance -= amount
        print(f"Current balance: {self._balance}")

    def show_balance(self):
        print(f"Current balance: {self._balance}")


#     История операций
# Доработайте класс BankAccount.
#     Каждая операция пополнения и снятия должна сохраняться в историю.
#     История должна быть доступна через property history только для чтения.
# История представляется в виде списка строк ("Deposit: 150", "Withdraw: 100" и т.д.).


class BankAccount:
    def __init__(self, owner: str, balance: float = 0):
        self._owner = owner
        self._balance = balance
        self._history = []

    def deposit(self, amount: float):
        if amount <= 0:
            print("Error: Amount must be positive.")
            return
        self._balance += amount
        self._history.append(f"Deposit: {amount}")
        print(f"Current balance: {self._balance}")

    def withdraw(self, amount: float):
        if amount <= 0:
            print("Error: Amount must be positive.")
            return
        if amount > self._balance:
            print("Error: Not enough funds.")
            print(f"Current balance: {self._balance}")
            return
        self._balance -= amount
        self._history.append(f"Withdraw: {amount}")
        print(f"Current balance: {self._balance}")

    def show_balance(self):
        print(f"Current balance: {self._balance}")

    @property
    def history(self):
        return self._history.copy()

