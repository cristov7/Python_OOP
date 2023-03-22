from project.formula_teams.formula_team import FormulaTeam
from typing import Dict


class MercedesTeam(FormulaTeam):
    @property   # getter
    def sponsors(self) -> Dict[str, Dict[int, int]]:
        sponsors_dict = {"Petronas": {1: 1_000_000, 3: 500_000},
                         "TeamViewer": {5: 100_000, 7: 50_000}}
        return sponsors_dict

    @property   # getter
    def expenses(self) -> int:
        expenses_per_race = 200_000
        return expenses_per_race
