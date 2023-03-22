from project.animals.animal import Bird
from typing import List
from project.food import Meat
from project.food import Vegetable
from project.food import Fruit
from project.food import Seed


class Owl(Bird):
    @staticmethod
    def make_sound() -> str:
        sound = "Hoot Hoot"
        return sound

    @property   # getter
    def specific_type_of_food(self) -> List[object]:
        food_list = [Meat]
        return food_list

    @property   # getter
    def increase_weight(self) -> float:
        kg_every_piece_of_food = 0.25
        return kg_every_piece_of_food


class Hen(Bird):
    @staticmethod
    def make_sound() -> str:
        sound = "Cluck"
        return sound

    @property   # getter
    def specific_type_of_food(self) -> List[object]:
        food_list = [Vegetable, Fruit, Meat, Seed]
        return food_list

    @property   # getter
    def increase_weight(self) -> float:
        kg_every_piece_of_food = 0.35
        return kg_every_piece_of_food
