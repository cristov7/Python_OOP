from abc import ABC, abstractmethod


class BaseRobot(ABC):   # AbstractBaseClass
    def __init__(self, name: str, kind: str, price: float, weight: int):
        self.name = name       # the name of the robot
        self.kind = kind       # the kind of the robot
        self.price = price     # the price of the robot
        self.weight = weight   # the weight in kilograms of the robot

    @property   # getter
    def name(self) -> str:
        return self.__name

    @name.setter   # setter
    def name(self, value: str) -> [ValueError, None]:
        if value == "" or value.isspace():
            raise ValueError("Robot name cannot be empty!")
        else:
            self.__name = value

    @property   # getter
    def kind(self) -> str:
        return self.__kind

    @kind.setter   # setter
    def kind(self, value: str) -> [ValueError, None]:
        if value == "" or value.isspace():
            raise ValueError("Robot kind cannot be empty!")
        else:
            self.__kind = value

    @property   # getter
    def price(self) -> float:
        return self.__price

    @price.setter   # setter
    def price(self, value: float) -> [ValueError, None]:
        if value <= 0.0:
            raise ValueError("Robot price cannot be less than or equal to 0.0!")
        else:
            self.__price = value

    @property                           # getter
    @abstractmethod                     # abstractmethod
    def increase_weight(self) -> int:   # must be implemented
        pass

    def eating(self) -> None:
        self.weight += self.increase_weight
