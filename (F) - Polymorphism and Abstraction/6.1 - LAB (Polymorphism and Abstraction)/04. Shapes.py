from abc import ABC, abstractmethod
from math import pi


class Shape(ABC):
    @abstractmethod
    def calculate_area(self):
        pass

    @abstractmethod
    def calculate_perimeter(self):
        pass


class Circle(Shape):
    def __init__(self, radius: int):
        self.__radius = radius

    def calculate_area(self):
        area = pi * self.__radius ** 2
        return area

    def calculate_perimeter(self):
        perimeter = 2 * pi * self.__radius
        return perimeter


class Rectangle(Shape):
    def __init__(self, height: int, width: int):
        self.__height = height
        self.__width = width

    def calculate_area(self):
        area = self.__height * self.__width
        return area

    def calculate_perimeter(self):
        perimeter = 2 * (self.__height + self.__width)
        return perimeter
