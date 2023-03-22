from project.animals.animal import Mammal
from typing import List
from project.food import Vegetable
from project.food import Fruit
from project.food import Meat


class Mouse(Mammal):
    @staticmethod
    def make_sound() -> str:
        sound = "Squeak"
        return sound

    @property   # getter
    def specific_type_of_food(self) -> List[object]:
        food_list = [Vegetable, Fruit]
        return food_list

    @property   # getter
    def increase_weight(self) -> float:
        kg_every_piece_of_food = 0.10
        return kg_every_piece_of_food


class Dog(Mammal):
    @staticmethod
    def make_sound() -> str:
        sound = "Woof!"
        return sound

    @property   # getter
    def specific_type_of_food(self) -> List[object]:
        food_list = [Meat]
        return food_list

    @property   # getter
    def increase_weight(self) -> float:
        kg_every_piece_of_food = 0.40
        return kg_every_piece_of_food


class Cat(Mammal):
    @staticmethod
    def make_sound() -> str:
        sound = "Meow"
        return sound

    @property   # getter
    def specific_type_of_food(self) -> List[object]:
        food_list = [Vegetable, Meat]
        return food_list

    @property   # getter
    def increase_weight(self) -> float:
        kg_every_piece_of_food = 0.30
        return kg_every_piece_of_food


class Tiger(Mammal):
    @staticmethod
    def make_sound() -> str:
        sound = "ROAR!!!"
        return sound

    @property   # getter
    def specific_type_of_food(self) -> List[object]:
        food_list = [Meat]
        return food_list

    @property   # getter
    def increase_weight(self) -> float:
        kg_every_piece_of_food = 1.00
        return kg_every_piece_of_food
