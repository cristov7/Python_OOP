class Mammal:
    __kingdom: str = "animals"   # private

    def __init__(self, name: str, type_mammal: str, sound: str):
        self.name = name
        self.type = type_mammal
        self.sound = sound

    def make_sound(self) -> str:
        return f"{self.name} makes {self.sound}"

    def get_kingdom(self) -> str:   # getter
        return self.__kingdom   # self.__kingdom == Mammal.__kingdom

    def info(self) -> str:
        return f"{self.name} is of type {self.type}"


# mammal = Mammal("Dog", "Domestic", "Bark")
# print(mammal.make_sound())
# print(mammal.get_kingdom())
# print(mammal.info())
