# # Open / Closed (OCP):


from abc import ABC, abstractmethod


class Animal(ABC):
    def __init__(self, species: str):
        self.species = species

    @staticmethod
    @abstractmethod
    def make_sound() -> str:
        pass


class Cat(Animal):
    @staticmethod
    def make_sound() -> str:
        sound = 'meow'
        return sound


class Dog(Animal):
    @staticmethod
    def make_sound() -> str:
        sound = 'woof-woof'
        return sound


class Chicken(Animal):
    @staticmethod
    def make_sound() -> str:
        sound = 'cluck'
        return sound


def animal_sound(animals: list):
    for animal in animals:
        print(animal.make_sound())
        # meow
        # woof - woof
        # cluck


# animals_list = [Cat("cat"), Dog("dog"), Chicken("chicken")]
# animal_sound(animals_list)
