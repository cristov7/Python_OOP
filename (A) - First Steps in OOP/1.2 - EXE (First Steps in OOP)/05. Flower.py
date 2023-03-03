class Flower:
    def __init__(self, name: str, water_requirements: int):
        self.name = name
        self.water_requirements = water_requirements
        self.is_happy: bool = False

    def water(self, quantity: int) -> None:
        if quantity >= self.water_requirements:
            self.is_happy = True

    def status(self) -> str:
        if self.is_happy:   # if self.is_happy == True:
            status_info = f"{self.name} is happy"
            return status_info
        else:   # elif self.is_happy == False:
            status_info = f"{self.name} is not happy"
            return status_info
        # return f"{self.name} is {'' if self.is_happy else 'not '}happy"


# flower = Flower("Lilly", 100)
# flower.water(50)
# print(flower.status())
# flower.water(60)
# print(flower.status())
# flower.water(100)
# print(flower.status())
