from typing import List


class Vet:
    animals: List[str] = []   # total amount of animals for all vets
    space: int = 5

    def __init__(self, name: str):
        self.name = name
        self.animals: List[str] = []

    def register_animal(self, animal_name: str) -> str:
        if len(self.animals) < Vet.space:
            self.animals.append(animal_name)
            Vet.animals.append(animal_name)
            return f"{animal_name} registered in the clinic"
        else:   # elif len(self.animals) >= Vet.space:
            return "Not enough space"

    def unregister_animal(self, animal_name: str) -> str:
        if animal_name in self.animals:
            self.animals.remove(animal_name)
            Vet.animals.remove(animal_name)
            return f"{animal_name} unregistered successfully"
        else:   # elif animal_name not in self.animals:
            return f"{animal_name} not in the clinic"

    def info(self) -> str:
        vet_name = self.name
        number_animals = len(self.animals)
        space_left_in_clinic = Vet.space - number_animals
        return f"{vet_name} has {number_animals} animals. {space_left_in_clinic} space left in clinic"


# peter = Vet("Peter")
# george = Vet("George")
# print(peter.register_animal("Tom"))
# print(george.register_animal("Cory"))
# print(peter.register_animal("Fishy"))
# print(peter.register_animal("Bobby"))
# print(george.register_animal("Kay"))
# print(george.unregister_animal("Cory"))
# print(peter.register_animal("Silky"))
# print(peter.unregister_animal("Molly"))
# print(peter.unregister_animal("Tom"))
# print(peter.info())
# print(george.info())
