# # Open / Closed (OCP):


from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def calculate_area(self) -> [int, float]:
        pass


class Rectangle(Shape):
    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height

    def calculate_area(self) -> int:
        area = self.width * self.height
        return area


class Triangle(Shape):
    def __init__(self, base: int, height: int):
        self.base = base
        self.height = height

    def calculate_area(self) -> float:
        area = self.base * self.height / 2
        return area


class AreaCalculator:
    def __init__(self, shapes: list):
        self.shapes = shapes

    @property   # getter
    def shapes(self):
        return self.__shapes

    @shapes.setter   # setter
    def shapes(self, value):
        if not isinstance(value, list):
            raise ValueError("`shapes` should be of type `list`.")
        else:
            self.__shapes = value

    @property   # getter
    def total_area(self):
        total = 0
        for shape in self.shapes:
            total += shape.calculate_area()
        return total


shapes = [Rectangle(1, 6), Triangle(2, 3)]
calculator = AreaCalculator(shapes)

print("The total area is: ", calculator.total_area)

# The total area is:  9.0
