class Student:
    def __init__(self, name: str | None = None, age: int | None = None):
        self.name = name
        self.age = age

    def set_age(self, value: int):
        if value <= 0:
            raise ValueError("Возраст должен быть положительным числом")
        self.age = value
