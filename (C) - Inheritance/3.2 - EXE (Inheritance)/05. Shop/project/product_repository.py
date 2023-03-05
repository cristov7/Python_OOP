from typing import List
from project.product import Product


class ProductRepository:
    def __init__(self):
        self.products: List[Product] = []   # [product_objects]

    def add(self, product: Product) -> None:   # product == product_object
        self.products.append(product)

    def find(self, product_name: str) -> [str, None]:
        product_objects_list = [product_object for product_object in self.products
                                if product_object.name == product_name]
        if product_objects_list:   # if len(product_objects_list) > 0:
            product_object = product_objects_list[0]
            return product_object   # product_object = product_name

    def remove(self, product_name: str) -> None:
        product_object = self.find(product_name)
        if product_object:   # if product is not None:
            self.products.remove(product_object)

    def __repr__(self) -> str:
        products_info = []
        for product_object in self.products:
            product_name = product_object   # product_object = product_object.name
            quantity = product_object.quantity
            product_info = f"{product_name}: {quantity}"
            products_info.append(product_info)
        return "\n".join(products_info)
