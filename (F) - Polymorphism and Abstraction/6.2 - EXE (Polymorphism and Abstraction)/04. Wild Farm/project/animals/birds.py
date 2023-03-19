from project.animals.animal import Bird
from project.food import Vegetable
from project.food import Fruit
from project.food import Meat
from project.food import Seed


class Owl(Bird):
    @property
    def food_that_eats(self):
        return [Meat]

    @property
    def gained_weight(self):
        return 0.25

    @staticmethod
    def make_sound():
        return "Hoot Hoot"


class Hen(Bird):
    @property
    def food_that_eats(self):
        return [Vegetable, Fruit, Meat, Seed]

    @property
    def gained_weight(self):
        return 0.35

    @staticmethod
    def make_sound():
        return "Cluck"
