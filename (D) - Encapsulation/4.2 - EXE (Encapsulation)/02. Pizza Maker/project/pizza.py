from project.dough import Dough
from typing import Dict
from project.topping import Topping


class Pizza:
    def __init__(self, name: str, dough: Dough, max_number_of_toppings: int):
        self.name = name
        self.dough = dough
        self.max_number_of_toppings = max_number_of_toppings
        self.toppings: Dict[str, float] = {}   # {"topping_type": "weight"}

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if value == "":
            raise ValueError("The name cannot be an empty string")
        else:
            self.__name = value

    @property
    def dough(self):
        return self.__dough

    @dough.setter
    def dough(self, value):
        if value is None:
            raise ValueError("You should add dough to the pizza")
        else:
            self.__dough = value

    @property
    def max_number_of_toppings(self):
        return self.__max_number_of_toppings

    @max_number_of_toppings.setter
    def max_number_of_toppings(self, value):
        if value <= 0:
            raise ValueError("The maximum number of toppings cannot be less or equal to zero")
        else:
            self.__max_number_of_toppings = value

    def add_topping(self, topping: Topping) -> [None, Exception]:   # topping = topping_object
        key = topping.topping_type
        value = topping.weight
        if key in self.toppings.keys():
            self.toppings[key] += value
        elif len(self.toppings) < self.max_number_of_toppings:
            self.toppings[key] = value
        else:
            raise ValueError("Not enough space for another topping")

    def calculate_total_weight(self) -> float:
        dough_weight = self.dough.weight
        topping_weight = sum(self.toppings.values())
        total_weight = dough_weight + topping_weight
        return total_weight
