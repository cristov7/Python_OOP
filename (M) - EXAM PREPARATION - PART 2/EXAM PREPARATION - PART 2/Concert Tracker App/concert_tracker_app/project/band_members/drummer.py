from project.band_members.musician import Musician
from typing import List


class Drummer(Musician):
    @property  # getter
    def available_types_of_skills(self) -> List[str]:   # implemented method
        return ["play the drums with drumsticks", "play the drums with drum brushes", "read sheet music"]
