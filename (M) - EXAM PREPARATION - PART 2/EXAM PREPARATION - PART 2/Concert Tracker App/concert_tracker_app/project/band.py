from typing import List
from project.band_members.musician import Musician


class Band:
    def __init__(self, name: str):
        self.name = name                    # the name of the band
        self.members: List[Musician] = []   # contain the members (musician objects) of the band

    @property   # getter
    def name(self) -> str:
        return self.__name

    @name.setter   # setter
    def name(self, value: str) -> [ValueError, None]:
        if value == "":
            raise ValueError("Band name should contain at least one character!")
        else:
            self.__name = value

    def __str__(self) -> str:
        name_of_the_band = self.name
        total_number_of_members = len(self.members)
        return f"{name_of_the_band} with {total_number_of_members} members."
