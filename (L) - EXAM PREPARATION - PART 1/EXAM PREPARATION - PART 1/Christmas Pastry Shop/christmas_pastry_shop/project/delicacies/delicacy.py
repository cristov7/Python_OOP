from abc import ABC, abstractmethod


class Delicacy(ABC):   # AbstractBaseClass
    def __init__(self, name: str, portion: int, price: float):
        self.name = name         # the name of a delicacy
        self.portion = portion   # the portion of a delicacy in grams
        self.price = price       # the price of a delicacy

    @property   # getter
    def name(self) -> str:
        return self.__name

    @name.setter   # setter
    def name(self, value) -> [ValueError, None]:
        if value.strip() == "":
            raise ValueError("Name cannot be null or whitespace!")
        else:
            self.__name = value

    @property   # getter
    def price(self) -> float:
        return self.__price

    @price.setter   # setter
    def price(self, value) -> [ValueError, None]:
        if value <= 0.0:
            raise ValueError("Price cannot be less or equal to zero!")
        else:
            self.__price = value

    @property   # getter
    @abstractmethod
    def get_portion(self) -> int:
        pass

    def details(self) -> str:
        product = self.__class__.__name__
        name = self.name
        portion = self.portion
        price = self.price
        return f"{product} {name}: {portion}g - {price:.2f}lv."
