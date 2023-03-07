class Person:
    def __init__(self, name: str, age: int):
        self.__name = name       # private
        self.__age = age         # private

    def get_name(self) -> str:   # getter
        return self.__name

    def get_age(self) -> int:    # getter
        return self.__age


# person = Person("George", 32)
# print(person.get_name())
# print(person.get_age())
