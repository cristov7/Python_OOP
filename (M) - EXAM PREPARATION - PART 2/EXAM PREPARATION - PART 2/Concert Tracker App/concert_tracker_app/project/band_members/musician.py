from abc import ABC, abstractmethod
from typing import List


class Musician(ABC):   # AbstractBaseClass
    def __init__(self, name: str, age: int):
        self.name = name              # the name of the musician
        self.age = age                # the age of the musician
        self.skills: List[str] = []   # contain all skills a musician has

    @property   # getter
    def name(self) -> str:
        return self.__name

    @name.setter   # setter
    def name(self, value: str) -> [ValueError, None]:
        if value.strip() == "":
            raise ValueError("Musician name cannot be empty!")
        else:
            self.__name = value

    @property   # getter
    def age(self) -> int:
        return self.__age

    @age.setter   # setter
    def age(self, value: int) -> [ValueError, None]:
        if value < 16:
            raise ValueError("Musicians should be at least 16 years old!")
        else:
            self.__age = value

    @property   # getter
    @abstractmethod
    def available_types_of_skills(self) -> List[str]:
        pass

    def learn_new_skill(self, new_skill: str) -> [ValueError, Exception, str]:
        if new_skill not in self.available_types_of_skills:
            raise ValueError(f"{new_skill} is not a needed skill!")
        elif new_skill in self.skills:
            raise Exception(f"{new_skill} is already learned!")
        else:
            self.skills.append(new_skill)
            musician_name = self.name
            return f"{musician_name} learned to {new_skill}."
