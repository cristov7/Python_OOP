from abc import ABC, abstractmethod


class Animal(ABC):
    def __init__(self, name: str, age: int, gender: str):
        self.name = name
        self.age = age
        self.gender = gender

    @staticmethod
    @abstractmethod
    def make_sound():
        pass

    def __repr__(self) -> str:
        name = self.name
        age = self.age
        gender = self.gender
        class_name = self.__class__.__name__
        return f"This is {name}. {name} is a {age} year old {gender} {class_name}"
