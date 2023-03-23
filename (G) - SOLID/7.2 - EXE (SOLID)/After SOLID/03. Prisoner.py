# # Liskov Substitution (LSP):


from typing import List
import copy


class Person:
    def __init__(self, position: List[int]):
        self.position = position


class FreePerson(Person):
    def walk_north(self, dist: int) -> None:
        self.position[1] += dist

    def walk_east(self, dist: int) -> None:
        self.position[0] += dist


class Prisoner(Person):
    PRISON_LOCATION: List[int] = [3, 3]

    def __init__(self):
        super().__init__(copy.copy(self.PRISON_LOCATION))
        self.is_free: bool = False


prisoner = Prisoner()
print("The prisoner trying to walk to north by 10 and east by -3.")

try:
    prisoner.walk_north(10)
    prisoner.walk_east(-3)
except:
    pass

print(f"The location of the prison: {prisoner.PRISON_LOCATION}")
print(f"The current position of the prisoner: {prisoner.position}")

# The prisoner trying to walk to north by 10 and east by -3.
# The location of the prison: (3, 3)
# The current position of the prisoner: (3, 3)
