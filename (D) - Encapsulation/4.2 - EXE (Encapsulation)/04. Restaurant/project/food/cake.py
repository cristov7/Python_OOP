from project.food.dessert import Dessert


class Cake(Dessert):
    PRICE: int = 5
    GRAMS: int = 250
    CALORIES: int = 1000

    def __init__(self, name: str):
        super().__init__(name, Cake.PRICE, Cake.GRAMS, Cake.CALORIES)
