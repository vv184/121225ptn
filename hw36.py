#     Класс Person
# Создайте класс Person, представляющий человека.
#     Каждый человек должен иметь имя.
# Добавьте метод introduce(), который выводит приветствие с именем.


class Person:
    def __init__(self, name):
        self.name = name

    def introduce(self):
        print(f"Hello, my name is {self.name}.")

p = Person("Alice")
p.introduce()


#     Класс Student
# На основе класса Person создайте класс Student.
#     Студент должен иметь имя и номер курса.
#     Метод introduce() должен сначала выводить базовое приветствие, а затем строку: I'm on course <номер_курса>.
# Пример вывода:


class Person:
    def __init__(self, name):
        self.name = name

    def introduce(self):
        print(f"Hello, my name is {self.name}.")


class Student(Person):
    def __init__(self, name, course):
        super().__init__(name)
        self.course = course

    def introduce(self):
        print(f"Hello, my name is {self.name}. I'm on course {self.course}.")


s = Student("Alice", 2)
s.introduce()


#     Класс Teacher и список людей
# На основе класса Person создайте класс Teacher.
#     У преподавателя есть имя и предмет.
#     Метод introduce() должен выводить имя и предмет.
#     Метод introduce() должен выводить строку: Hello, I am professor <имя>. My subject is <предмет>.
#     Создайте список, в котором будут Student и Teacher, и вызовите у всех метод introduce().


class Person:
    def __init__(self, name):
        self.name = name

    def introduce(self):
        print(f"Hello, my name is {self.name}.")


class Student(Person):
    def __init__(self, name, course):
        super().__init__(name)
        self.course = course

    def introduce(self):
        print(f"Hello, my name is {self.name}. I'm on course {self.course}.")


class Teacher(Person):
    def __init__(self, name, subject):
        super().__init__(name)
        self.subject = subject

    def introduce(self):
        print(f"Hello, I am professor {self.name}. My subject is {self.subject}.")


people = [
    Student("Alice", 2),
    Teacher("Bob", "Mathematics")
]

for person in people:
    person.introduce()