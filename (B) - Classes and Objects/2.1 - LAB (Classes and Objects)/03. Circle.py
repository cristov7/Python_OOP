class Circle:
    pi: float = 3.14

    def __init__(self, radius: int):
        self.radius = radius

    def set_radius(self, new_radius: int) -> None:
        self.radius = new_radius

    def get_area(self) -> [float, int]:
        area = Circle.pi * self.radius ** 2   # Circle.pi == self.pi
        return area

    def get_circumference(self) -> [float, int]:
        circumference = 2 * Circle.pi * self.radius   # Circle.pi == self.pi
        return circumference


# circle = Circle(10)
# circle.set_radius(12)
# print(circle.get_area())
# print(circle.get_circumference())
