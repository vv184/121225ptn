#     Счётчик экземпляров
# Создайте класс User, представляющий пользователя.
#     При создании должны указываться логин (username) и пароль (password).
#     У класса должно быть поле total_users, хранящее общее количество созданных пользователей.
#     При каждом создании нового объекта User, счётчик должен увеличиваться.
#     Добавьте метод get_total(), возвращающий количество пользователей.
#     Проверьте, что счётчик работает.


class User:
    total_users = 0

    def __init__(self, username, password):
        self.username = username
        self.password = password
        User.total_users += 1

    @classmethod
    def get_total(cls):
        return cls.total_users


u1 = User("alice", "1234")
u2 = User("bob", "5678")

print("Total users:", User.get_total())


#     Проверка данных пользователя
# Доработайте класс User.
#     Добавьте валидации полей при создании.
#     Имя должно быть непустой строкой.
#     Пароль должен быть строкой длиной не менее 5 символов.
#     Если данные некорректны — выбрасывайте ValueError.
#     Добавьте строковое представление объекта.
#     Проверьте работу класса с разными значениями.


class User:
    total_users = 0

    def __init__(self, username, password):
        if not isinstance(username, str) or username.strip() == "":
            raise ValueError(f"Invalid username: {username}")

        if not isinstance(password, str) or len(password) < 5:
            raise ValueError(f'Invalid password: "{password}"')

        self.username = username
        self.password = password
        User.total_users += 1

    def __str__(self):
        return f"User: {self.username}"


# ВАЖНО: это должно быть ВНЕ класса
user1 = User("alice", "secret")
print(user1)

try:
    user2 = User("bob", "qwe")
except ValueError as e:
    print("ValueError:", e)