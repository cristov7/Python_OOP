from typing import Dict


class Shop:
    def __init__(self, name: str, type_shop: str, capacity: int):
        self.name = name
        self.type = type_shop
        self.capacity = capacity
        self.items: Dict[str, int] = {}   # {item_names: quantities}

    @classmethod
    def small_shop(cls, name: str, type_shop: str):
        return cls(name, type_shop, 10)

    def add_item(self, item_name: str) -> str:
        current_quantity = sum(self.items.values())
        if current_quantity < self.capacity:
            if item_name in self.items.keys():
                self.items[item_name] += 1
            else:
                self.items[item_name] = 1
            return f"{item_name} added to the shop"
        else:
            return "Not enough capacity in the shop"

    def remove_item(self, item_name: str, amount: int) -> str:
        if item_name in self.items.keys():
            current_quantity = self.items[item_name]
            if current_quantity > amount:
                self.items[item_name] -= amount
                return f"{amount} {item_name} removed from the shop"
            elif current_quantity == amount:
                del self.items[item_name]
                return f"{amount} {item_name} removed from the shop"
            else:
                return f"Cannot remove {amount} {item_name}"
        else:
            return f"Cannot remove {amount} {item_name}"

    def __repr__(self) -> str:
        shop_name = self.name
        shop_type = self.type
        shop_capacity = self.capacity
        return f"{shop_name} of type {shop_type} with capacity {shop_capacity}"


# fresh_shop = Shop("Fresh Shop", "Fruit and Veg", 50)
# small_shop = Shop.small_shop("Fashion Boutique", "Clothes")
# print(fresh_shop)
# print(small_shop)
#
# print(fresh_shop.add_item("Bananas"))
# print(fresh_shop.remove_item("Tomatoes", 2))
#
# print(small_shop.add_item("Jeans"))
# print(small_shop.add_item("Jeans"))
# print(small_shop.remove_item("Jeans", 2))
# print(small_shop.items)
