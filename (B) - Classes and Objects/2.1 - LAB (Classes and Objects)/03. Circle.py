class Circle:
    pi = 3.14

    def __init__(self, radius: int):
        self.radius = radius

    def set_radius(self, new_radius: int) -> None:
        self.radius = new_radius

    def get_area(self) -> [int, float]:
        return Circle.pi * self.radius ** 2   # Circle.pi == self.pi

    def get_circumference(self) -> [int, float]:
        return 2 * Circle.pi * self.radius   # Circle.pi == self.pi


# circle = Circle(10)
# circle.set_radius(12)
# print(circle.get_area())
# print(circle.get_circumference())
