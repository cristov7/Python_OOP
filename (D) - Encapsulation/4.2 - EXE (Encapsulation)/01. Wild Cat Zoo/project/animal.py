class Animal:
    def __init__(self, name: str, gender: str, age: int, money_for_care: int):
        self.name = name
        self.gender = gender
        self.age = age
        self.money_for_care = money_for_care

    def __repr__(self) -> str:
        name = self.name
        age = self.age
        gender = self.gender
        return f"Name: {name}, Age: {age}, Gender: {gender}"
