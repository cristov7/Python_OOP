from project.band_members.musician import Musician
from typing import List


class Singer(Musician):
    @property   # getter
    def available_types_of_skills(self) -> List[str]:   # implemented method
        return ["sing high pitch notes", "sing low pitch notes"]
