from typing import List
from project.product import Product


class ProductRepository:
    def __init__(self):
        self.products: List[Product] = []   # [product_objects]

    def add(self, product: Product) -> None:
        self.products.append(product)

    def find(self, product_name: str) -> [object, None]:
        product_list = [product_object for product_object in self.products
                        if product_object.name == product_name]
        if product_list:   # if len(product_list) > 0:
            product = product_list[0]
            return product

    def remove(self, product_name: str) -> None:
        product = self.find(product_name)
        if product:   # if product is not None:
            self.products.remove(product)

    def __repr__(self) -> str:
        products_info = []
        for product_object in self.products:
            product_name = product_object
            quantity = product_object.quantity
            product_info = f"{product_name}: {quantity}"
            products_info.append(product_info)
        return "\n".join(products_info)
