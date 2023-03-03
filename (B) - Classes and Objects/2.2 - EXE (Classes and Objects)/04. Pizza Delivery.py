from typing import Dict


class PizzaDelivery:
    def __init__(self, name: str, price: float, ingredients: Dict[str, int]):
        self.name = name
        self.price = price
        self.ingredients = ingredients   # {ingredient: quantity}
        self.ordered: bool = False

    def add_extra(self, ingredient: str, quantity: int, price_per_quantity: float) -> [None, str]:
        if not self.ordered:   # if self.ordered == False:
            self.price += quantity * price_per_quantity
            if ingredient in self.ingredients.keys():
                self.ingredients[ingredient] += quantity
            else:
                self.ingredients[ingredient] = quantity
        else:   # elif self.ordered == True:
            pizza_name = self.name
            return f"Pizza {pizza_name} already prepared, and we can't make any changes!"

    def remove_ingredient(self, ingredient: str, quantity: int, price_per_quantity: float) -> [str, None]:
        if not self.ordered:   # if self.ordered == False:
            if ingredient not in self.ingredients.keys():
                pizza_name = self.name
                return f"Wrong ingredient selected! We do not use {ingredient} in {pizza_name}!"
            else:
                quantity_in_pizza = self.ingredients[ingredient]
                if quantity > quantity_in_pizza:
                    return f"Please check again the desired quantity of {ingredient}!"
                else:
                    self.ingredients[ingredient] -= quantity
                    self.price -= quantity * price_per_quantity
        else:   # elif self.ordered == True:
            pizza_name = self.name
            return f"Pizza {pizza_name} already prepared, and we can't make any changes!"

    def make_order(self) -> str:
        self.ordered = True
        pizza_name = self.name
        ingredient_with_quantity = ", ".join([f"{ingredient}: {quantity}"
                                              for ingredient, quantity in self.ingredients.items()])
        price = self.price
        return f"You've ordered pizza {pizza_name} prepared with {ingredient_with_quantity} " \
               f"and the price will be {price}lv."


# margarita = PizzaDelivery('Margarita', 11, {'cheese': 2, 'tomatoes': 1})
# margarita.add_extra('mozzarella', 1, 0.5)
# margarita.add_extra('cheese', 1, 1)
# margarita.remove_ingredient('cheese', 1, 1)
# print(margarita.remove_ingredient('bacon', 1, 2.5))
# print(margarita.remove_ingredient('tomatoes', 2, 0.5))
# margarita.remove_ingredient('cheese', 2, 1)
# print(margarita.make_order())
# print(margarita.add_extra('cheese', 1, 1))
