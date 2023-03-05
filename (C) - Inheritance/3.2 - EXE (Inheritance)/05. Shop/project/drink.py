from project.product import Product


class Drink(Product):
    QUANTITY: int = 10

    def __init__(self, name: str):
        super().__init__(name, Drink.QUANTITY)
