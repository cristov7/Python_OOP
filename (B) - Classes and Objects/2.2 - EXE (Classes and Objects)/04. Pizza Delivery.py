from typing import Dict


class PizzaDelivery:
    def __init__(self, name: str, price: float, ingredients: Dict[str: int]):
        self.name = name
        self.price = price
        self.ingredients = ingredients
        self.ordered = False

    def add_extra(self, ingredient: str, quantity: int, price_per_quantity: float) -> [str, None]:
        if self.ordered:   # if self.ordered == True:
            return f"Pizza {self.name} already prepared, and we can't make any changes!"
        else:  # elif self.ordered == False:
            self.price += price_per_quantity * quantity
            if ingredient in self.ingredients.keys():
                self.ingredients[ingredient] += quantity
            else:
                self.ingredients[ingredient] = quantity

    def remove_ingredient(self, ingredient: str, quantity: int, price_per_quantity: float) -> [str, None]:
        if self.ordered:   # if self.ordered == True:
            return f"Pizza {self.name} already prepared, and we can't make any changes!"
        else:   # elif self.ordered == False:
            if ingredient not in self.ingredients.keys():
                return f"Wrong ingredient selected! We do not use {ingredient} in {self.name}!"
            else:
                quantity_in_pizza = self.ingredients[ingredient]
                if quantity > quantity_in_pizza:
                    return f"Please check again the desired quantity of {ingredient}!"
                else:
                    self.ingredients[ingredient] -= quantity
                    self.price -= price_per_quantity * quantity

    def make_order(self) -> str:
        self.ordered = True
        pizza_name = self.name
        ingredients_info = ", ".join([f"{ingredient}: {quantity}"
                                      for ingredient, quantity in self.ingredients.items()])
        price = self.price
        return f"You've ordered pizza {pizza_name} prepared with {ingredients_info} and the price will be {price}lv."


# margarita = PizzaDelivery('Margarita', 11, {'cheese': 2, 'tomatoes': 1})
# margarita.add_extra('mozzarella', 1, 0.5)
# margarita.add_extra('cheese', 1, 1)
# margarita.remove_ingredient('cheese', 1, 1)
# print(margarita.remove_ingredient('bacon', 1, 2.5))
# print(margarita.remove_ingredient('tomatoes', 2, 0.5))
# margarita.remove_ingredient('cheese', 2, 1)
# print(margarita.make_order())
# print(margarita.add_extra('cheese', 1, 1))
