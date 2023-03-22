from abc import ABC, abstractmethod
from typing import List
from project.food import Food


class Animal(ABC):
    def __init__(self, name: str, weight: float):
        self.name = name
        self.weight = weight
        self.food_eaten: int = 0

    @staticmethod
    @abstractmethod
    def make_sound() -> str:
        pass

    @property   # getter
    @abstractmethod
    def specific_type_of_food(self) -> List[object]:
        pass
    
    @property   # getter
    @abstractmethod
    def increase_weight(self) -> float:
        pass

    def feed(self, food: Food) -> [None, str]:   # food == food_object
        if type(food) in self.specific_type_of_food:
            self.weight += food.quantity * self.increase_weight
            self.food_eaten += food.quantity
        else:
            animal_type = self.__class__.__name__
            food_type = food.__class__.__name__
            return f"{animal_type} does not eat {food_type}!"


class Bird(Animal, ABC):
    def __init__(self, name: str, weight: float, wing_size: float):
        super().__init__(name, weight)
        self.wing_size = wing_size

    # @staticmethod
    # @abstractmethod
    # def make_sound() -> str:
    #     pass

    # @property   # getter
    # @abstractmethod
    # def specific_type_of_food(self) -> List[object]:
    #     pass

    # @property   # getter
    # @abstractmethod
    # def increase_weight(self) -> float:
    #     pass

    def __repr__(self) -> str:
        animal_type = self.__class__.__name__
        animal_name = self.name
        wing_size = self.wing_size
        animal_weight = self.weight
        food_eaten = self.food_eaten
        return f"{animal_type} [{animal_name}, {wing_size}, {animal_weight}, {food_eaten}]"


class Mammal(Animal, ABC):
    def __init__(self, name: str, weight: float, living_region: str):
        super().__init__(name, weight)
        self.living_region = living_region

    # @staticmethod
    # @abstractmethod
    # def make_sound() -> str:
    #     pass

    # @property   # getter
    # @abstractmethod
    # def specific_type_of_food(self) -> List[object]:
    #     pass

    # @property   # getter
    # @abstractmethod
    # def increase_weight(self) -> float:
    #     pass

    def __repr__(self) -> str:
        animal_type = self.__class__.__name__
        animal_name = self.name
        animal_weight = self.weight
        animal_living_region = self.living_region
        food_eaten = self.food_eaten
        return f"{animal_type} [{animal_name}, {animal_weight}, {animal_living_region}, {food_eaten}]"
