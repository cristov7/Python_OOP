from project.band_members.musician import Musician
from typing import List


class Guitarist(Musician):
    @property   # getter
    def available_types_of_skills(self) -> List[str]:   # implemented method
        return ["play metal", "play rock", "play jazz"]
