from project.formula_teams.formula_team import FormulaTeam
from typing import Dict


class RedBullTeam(FormulaTeam):
    @property   # getter
    def sponsors(self) -> Dict[str, Dict[int, int]]:
        sponsors_dict = {"Oracle": {1: 1_500_000, 2: 800_000},
                         "Honda": {8: 20_000, 10: 10_000}}
        return sponsors_dict

    @property   # getter
    def expenses(self) -> int:
        expenses_per_race = 250_000
        return expenses_per_race
